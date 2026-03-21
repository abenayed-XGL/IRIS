---
title: Home
nav:
  order: 0
---

# About IRIS Lab
The Intelligent Radio and Integrated Systems (IRIS) Laboratory, led by Assistant Professor Ahmed Ben Ayed, is part of the Department of Electronic and Computer Engineering at the Hong Kong University of Science and Technology (HKUST).

Current research activities include the design of power amplifiers and frequency-multiplier-based transmitters for mm-wave and sub-THz signal generation, phased and large-scale antenna arrays that explicitly account for hardware non-idealities, advanced signal processing techniques for calibration, beamforming, and linearization, and the development of novel measurement methodologies for wideband modulated signal characterization.

A defining feature of the IRIS Lab is its system-level approach: integrated circuits, antenna arrays, digital signal processing, and measurement techniques are developed in a tightly coupled manner to ensure that theoretical advances translate into practical, deployable RF systems.

{% include section.html %}

## Principal Investigator

{% assign pi = site.members | where: "name", "Ahmed Ben Ayed" | first %}

{% if pi %}

  {% capture floatcontent %}

  {% include portrait.html lookup=pi.slug %}

  <div>
    {% for link in pi.links %}
      {% assign key = link[0] %}
      {% assign value = link[1] %}
      {% include button.html type=key link=value style="bare" %}<br>
    {% endfor %}
  </div>

  {% endcapture %}

  {% include float.html content=floatcontent %}

  {{ pi.content }}

{% else %}
  <p><em>PI profile not found. Check the collection name and PI identifier.</em></p>
{% endif %}


## Highlights

{% capture text %}

The IRIS Lab develops next-generation high-frequency RF circuits and systems for wireless and SATCOM applications. Our research focuses on the integration of signal processing, antenna and circuit design, and advanced test and measurement techniques to enable efficient, high-performance communication platforms.

{%
  include button.html
  link="research"
  text="See our research"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}

{% endcapture %}

{%
  include feature.html
  image="images/research.svg"
  link="research"
  title="Our Research"
  text=text
%}

{% capture text %}

Members of the IRIS Lab develop a strong system-level understanding of RF technologies and gain hands-on experience that prepares them for careers in academia and industry.

{%
  include button.html
  link="team"
  text="Meet our team"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}

{% endcapture %}

{%
  include feature.html
  image="images/team.svg"
  link="team"
  title="Our Team"
  text=text
  flip=true
%}

{% capture text %}

The IRIS Lab welcomes undergraduate students, prospective postgraduate students, and collaborators with interests in RF circuits and systems, antenna arrays, signal processing, and test and measurement science.

{%
  include button.html
  link="contact"
  text="Join us"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}

{% endcapture %}

{%
  include feature.html
  image="images/join.svg"
  link="contact"
  title="Join Us"
  text=text
%}
