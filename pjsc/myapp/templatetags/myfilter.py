from django import template

register = template.Library()

'''过滤器'''


@register.filter()
def get_value_filter(mydict, key):
    try:
        return mydict[key]
    except:
        return '必须是字典，而且必须key存在'
