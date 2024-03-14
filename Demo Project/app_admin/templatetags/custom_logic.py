from django import template
register = template.Library()

@register.filter
def multiply_three(value, arg1, arg2):
    if None in (value, arg1, arg2):
        return None
    try:
        result = float(value) * float(arg1) * float(arg2)
        return result
    except ValueError:
        return None


@register.filter
def mul(a,b):
    return a*b


@register.filter
def getStttt(total,a):
   
    return total+a





# @register.filter
# def div(a,b):
#     return a/b