from django import template
from app.models import Provincia

register = template.Library()

@register.inclusion_tag('app/provincias.html')
def get_provincias_list():
    return {'provincias': Provincia.objects.all()}