---
title: Home
nav:
  order: 0
---

# About RF-SI Laboratory
The RF Systems Integration (RF-SI) Laboratory is a research group led by Assistant Professor Ahmed Ben Ayed in the Department of Electronic and Computer Engineering at the Hong Kong University of Science and Technology (HKUST).

Current research activities include the design of power amplifiers and frequency-multiplier-based transmitters for mm-wave and sub-THz signal generation, phased and large-scale antenna arrays that explicitly account for hardware non-idealities, advanced signal processing techniques for calibration, beamforming, and linearization, and the development of novel measurement methodologies for wideband modulated signal characterization.

A defining feature of the RF-SI Laboratory is its system-level approach: integrated circuits, antenna arrays, digital signal processing, and measurement techniques are developed in a tightly coupled manner to ensure that theoretical advances translate into practical, deployable RF systems.

{% include section.html %}

# About the PI

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

RF-SI Laboratory focuses on the development of high-frequency RF systems through the integration of hardware design, signal processing, and experimental validation. Our research activities are motivated by applications in 5G/6G wireless communications, satellite communications (SATCOM), and emerging high-frequency sensing systems.

{%
  include button.html
  link="research"
  text="See our publications"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}

{% endcapture %}

{%
  include feature.html
  image="images/photo.svg"
  link="research"
  title="Our Research"
  text=text
%}

{% capture text %}

Members of the RF-SI Laboratory are trained to develop a strong system-level understanding of RF technologies and are well positioned for careers in academia and industry, particularly in high-frequency wireless, satellite, and measurement-oriented engineering roles.

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
  image="images/photo.svg"
  link="team"
  title="Our Team"
  text=text
%}
