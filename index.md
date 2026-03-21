---
title: Home
nav:
  order: 0
---

# Our Mission
The Intelligent Radio and Integrated Systems (IRIS) Laboratory within the Department of Electronic and Computer Engineering is dedicated to advancing next-generation high-frequency RF circuits and systems for wireless and satellite communications.

Its mission is to bridge the gap between theoretical innovation and practical deployment by co-developing RF circuits and antenna arrays, signal processing algorithms, and measurement techniques as part of a unified system-level design effort.

Through this work, IRIS aims to make future communication systems more efficient, reliable, and scalable.

# Our Approach

IRIS employs a system-level approach that spans circuit design, antenna design, digital signal processing, and test and measurement science.

Under the leadership of Prof. Ahmed Ben Ayed, our team turns research ideas into high-impact prototypes and publications using state-of-the-art design tools and measurement equipment.

Our industry-focused, collaborative approach to research is designed to train the next generation of highly qualified RF engineers and researchers.


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

Our members develop a strong system-level understanding of RF technologies and gain hands-on experience that prepares them for careers in academia and industry.

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

IRIS welcomes undergraduate and prospective postgraduate students as well as collaborators with interests in RF circuits, antenna arrays, signal processing, and test and measurement. 

{%
  include button.html
  link="contact"
  text="Join Us"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}

{% endcapture %}

{%
  include feature.html
  image="images/join.svg"
  link="contact"
  title="Opportunities"
  text=text
%}
