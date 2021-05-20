from django import template
from django.template import Context
from django.template import Template

register = template.Library()

KEY_VALUE_TEMPLATE = Template("{{ key }}={{ value }}")


@register.filter
def to_keyvalues(dictionary):
    return [KEY_VALUE_TEMPLATE.render(Context({'key': key, 'value': value})) for key, value in dictionary.items()]


@register.filter
def to_import(class_name):
    modules = class_name.split('.')
    return '.'.join(modules[:-1]), modules[-1]


@register.filter
def to_classnames(classes):
    return [cl.split('.')[-1] for cl in classes]


@register.filter
def to_permission_codes(permission_codes, **kwargs):
    return permission_codes
