from django import template

register = template.Library()

@register.filter
def split_text(value):
    return value.split("~")
