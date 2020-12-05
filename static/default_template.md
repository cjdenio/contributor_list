## 👥 Contributors

{% for contributor in contributors %}
- **[@{{ contributor.login }}]({{ contributor.html_url }})**{% if contributor.contributions %} ({{ contributor.contributions }} contribution{% if contributor.contributions > 1 %}s{% endif %}){% endif %}
{% endfor %}
