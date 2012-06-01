# -*- coding: utf-8 -*-
from django import template
register = template.Library()

@register.inclusion_tag('django_google_cse/searchform.html')
def load_searchform():
    return {}