from django import template

register = template.Library()

@register.filter
def get_obj_attr(obj, attr):
    print(obj.get(attr))
    if obj.get(attr):
        return obj[attr]
    else:
        return 'icon_default'
