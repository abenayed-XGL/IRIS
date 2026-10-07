"""
Build _data/patents.yaml from the "patent" works on the lab's ORCID record(s).

Runs at the end of cite.py (weekly citation update). Patents are linked to ORCID
through The Lens (orcid.org -> Works -> Add -> Search & link -> The Lens).
"""

import json
import re
from urllib.request import Request, urlopen
from util import *

ORCID_API = "https://pub.orcid.org/v3.0"
HEADERS = {"Accept": "application/json"}

OFFICES = {
    "US": "USPTO",
    "CN": "CNIPA",
    "EP": "EPO",
    "WO": "WIPO",
    "JP": "JPO",
    "KR": "KIPO",
    "CA": "CIPO",
    "GB": "UKIPO",
    "DE": "DPMA",
    "AU": "IP Australia",
    "HK": "HKIPD",
    "TW": "TIPO",
}


def fetch(path):
    request = Request(url=f"{ORCID_API}/{path}", headers=HEADERS)
    return json.loads(urlopen(request, timeout=30).read())


def parse_number(value):
    """'US 11,234,567 B2' / 'US20210123456A1' / 'WO 2022/123456 A1' -> (country, digits, kind)"""
    compact = re.sub(r"[\s,/._-]", "", str(value or "").upper())
    match = re.match(r"^([A-Z]{2})(\d+)([A-Z]\d?)?$", compact)
    if not match:
        return None
    return match.group(1), match.group(2), match.group(3) or ""


def display_number(country, digits, kind):
    if country == "US" and len(digits) <= 8:
        digits = f"{int(digits):,}"
    elif country == "US" and len(digits) == 11:
        digits = f"{digits[:4]}/{digits[4:]}"
    elif country == "WO" and len(digits) == 10:
        digits = f"{digits[:4]}/{digits[4:]}"
    return " ".join(part for part in [country, digits, kind] if part)


def status_of(country, kind):
    if country == "WO":
        return "PCT application"
    if country == "CN" and kind.startswith("U"):
        return "Granted"  # utility model
    if kind[:1] in ("B", "C", "E", "S"):
        return "Granted"
    return "Application"


SMALL_WORDS = {"a", "an", "and", "as", "at", "by", "for", "in", "of", "on", "or", "the", "to", "via", "with"}
ACRONYMS = {"RF", "MIMO", "DPD", "OTA", "PA", "PAS", "5G", "6G", "ADC", "DAC", "VNA", "EVM", "PCB", "MMIC", "LTE", "IQ", "I/Q", "MM-WAVE", "SATCOM"}


def title_case(text):
    """Patent offices often supply titles in ALL CAPS; convert to normal title case."""
    if not text or text != text.upper():
        return text
    words = text.split()
    out = []
    for i, word in enumerate(words):
        if word in ACRONYMS:
            out.append({"PAS": "PAs", "MM-WAVE": "mm-Wave"}.get(word, word))
        elif "/" in word:
            out.append("/".join(w.lower() if w.lower() in SMALL_WORDS else w.capitalize() for w in word.split("/")))
        elif i > 0 and word.lower() in SMALL_WORDS:
            out.append(word.lower())
        else:
            out.append("-".join(w.capitalize() for w in word.split("-")))
    return " ".join(out)


def known_authors():
    """Author names as written on the lab's papers, keyed by their set of name parts."""
    names = {}
    try:
        for citation in load_data("_data/citations.yaml") or []:
            for author in get_safe(citation, "authors", []) or []:
                names.setdefault(frozenset(str(author).lower().split()), author)
    except Exception:
        pass
    return names


def tidy_name(name, names):
    """'Ayed Ahmed Ben' -> 'Ahmed Ben Ayed' when that person appears on a paper."""
    match = names.get(frozenset(name.lower().split()))
    if match:
        return match
    return name.title() if name == name.upper() else name


def build(orcid_ids):
    patents = []
    names = known_authors()
    for orcid in orcid_ids:
        groups = get_safe(fetch(f"{orcid}/works"), "group", [])
        for group in groups:
            summaries = get_safe(group, "work-summary", [])
            summary = next((s for s in summaries if get_safe(s, "type", "") == "patent"), None)
            if not summary:
                continue

            # full record has inventors and more identifiers
            try:
                work = fetch(f"{orcid}/work/{get_safe(summary, 'put-code', '')}")
            except Exception:
                work = summary

            ids = get_safe(work, "external-ids.external-id", []) or []
            number = None
            lens_id = None
            for _id in ids:
                id_type = str(get_safe(_id, "external-id-type", "")).lower()
                value = get_safe(_id, "external-id-value", "")
                if id_type in ("pat", "patent", "patent-number") and not number:
                    number = parse_number(value)
                if id_type == "lensid":
                    lens_id = value
            if not number:
                # some sources put the number in the title or url
                for text in [get_safe(work, "url.value", ""), get_safe(work, "title.title.value", "")]:
                    found = re.search(r"\b([A-Z]{2}[\s-]?\d[\d,/\s]{5,}\d[\s-]?[A-Z]\d?)\b", str(text))
                    if found:
                        number = parse_number(found.group(1))
                        break

            year = get_safe(work, "publication-date.year.value", "")
            month = get_safe(work, "publication-date.month.value", "") or "01"
            day = get_safe(work, "publication-date.day.value", "") or "01"
            date = format_date(f"{year}-{month}-{day}") if year else ""

            inventors = [
                get_safe(c, "credit-name.value", "")
                for c in get_safe(work, "contributors.contributor", []) or []
            ]
            inventors = [tidy_name(name, names) for name in inventors if name]

            patent = {"title": title_case(get_safe(work, "title.title.value", "")) or "[untitled patent]"}
            if number:
                country, digits, kind = number
                patent["number"] = display_number(country, digits, kind)
                patent["office"] = OFFICES.get(country, country)
                patent["status"] = status_of(country, kind)
                patent["link"] = f"https://patents.google.com/patent/{country}{digits}{kind}"
            else:
                patent["status"] = "Patent"
            if not patent.get("link"):
                url = get_safe(work, "url.value", "")
                patent["link"] = url or (f"https://www.lens.org/lens/patent/{lens_id}" if lens_id else "")
            if date:
                patent["date"] = date
            if inventors:
                patent["inventors"] = inventors

            patents.append(patent)

    patents.sort(key=lambda p: p.get("date", ""), reverse=True)
    return patents


def main(output_file="_data/patents.yaml"):
    orcid_ids = [get_safe(e, "orcid", "") for e in load_data("_data/orcid.yaml")]
    patents = build([o for o in orcid_ids if o])
    save_data(output_file, patents)
    for p in patents:
        # visible in the GitHub Actions run summary
        print(f"::notice title=Patent::{p.get('number', '')} | {p.get('title', '')}", flush=True)
    return len(patents)
