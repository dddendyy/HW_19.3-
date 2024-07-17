from django import template

register = template.Library()


@register.filter()
def get_item(dictionary, key):
    return dictionary.get(key)


@register.filter()
def media_filter(path):
    if path:
        return f'/{path}'
    return f'#'


@register.filter()
def cut_string(string, number):
    return str(string)[8:number+2]
