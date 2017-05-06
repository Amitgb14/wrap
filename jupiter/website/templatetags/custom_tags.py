from django import template

register = template.Library()

@register.filter
def change(flg):
    if flg:
        return "Yes"
    else:
        return "No"
