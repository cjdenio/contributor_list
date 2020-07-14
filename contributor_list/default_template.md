## Contributors

{% for contributor in contributors %}
- [@{{ contributor.login }}]({{ contributor.html_url }}) ({{ contributor.contributions }} contribution{{ "s" if contributor.contributions != 1 }})
{% endfor %}