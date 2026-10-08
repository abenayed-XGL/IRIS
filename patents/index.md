---
title: Patents
nav:
  order: 2.5
  tooltip: Patents and patent applications
---

# {% include icon.html icon="fa-solid fa-certificate" %} Patents
Research by the Intelligent Radio and Integrated Systems (IRIS) Laboratory members leads to inventions with direct industrial relevance. Below are patents and patent applications invented or co-invented by members of the laboratory.

{% assign patents = site.data.patents | sort: "date" | reverse %}

{% if patents.size > 0 %}
  {% for patent in patents %}
    {% include patent.html patent=patent %}
  {% endfor %}
{% else %}
  {% include alert.html type="info" content="Patents will appear here after the next automatic update." %}
{% endif %}
