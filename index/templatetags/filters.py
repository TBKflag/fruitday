#coding=utf-8

from django import template
register = template.Library()

register = template.Library()  # register的名字是固定的,不可改变

@register.filter
def mod(v, n):
    return v % n
