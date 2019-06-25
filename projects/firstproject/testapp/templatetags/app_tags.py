from django import template
import datetime
register=template.Library()
@register.simple_tag(name="getdate")
def get_date():
    seo=datetime.datetime.now()
    return seo
@register.filter
def quotes(value):
  s='"'+value+'"'
  return s
