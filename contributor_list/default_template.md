## 👥 Contributors

{% for contributor in contributors %}
- <img src="{{ contributor.avatar_url }}" width="70" /> **[@{{ contributor.login }}]({{ contributor.html_url }})** ({{ contributor.contributions }} contribution{{ "s" if contributor.contributions != 1 }})
{% endfor %}