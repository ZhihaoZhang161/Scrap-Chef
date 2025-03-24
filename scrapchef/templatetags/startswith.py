# found at https://medium.com/@malvin.lok/add-a-custom-function-startwith-on-the-django-template-f11e1916f0d1
from django import template
register = template.Library()

@register.filter('startswith')
def startswith(text, starts):
    if isinstance(text, str):
        return text.startswith(starts)
    return False