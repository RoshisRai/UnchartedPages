from django import template

register = template.Library()

@register.filter(name='split')
# @stringfilter
def split(string, sep):
    """Return the string split by sep.

    Example usage: {{ value|split:"/" }}
    """
    return string.split(sep)