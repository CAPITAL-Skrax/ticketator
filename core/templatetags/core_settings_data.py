from django import template
from django.conf import settings as settings_file
from core.models import State


register = template.Library()
#register = template.Library('site_vars':site_vars)

@register.simple_tag
def site_vars():
	site_vars_data = {}
 	site_vars_data['name']=settings_file.SITE_NAME
 	site_vars_data['version']=settings_file.SITE_VERSION
 	site_vars_data['debug']=settings_file.DEBUG
 	return site_vars_data

@register.simple_tag
def all_states():
	state_objs = State.objects.all()
	return state_objs

@register.simple_tag
def status_name(status_id):
	status_obj_name = State.objects.get(id=status_id)
	return status_obj_name.name

@register.filter(name='addcss')
def addcss(field, css):
   return field.as_widget(attrs={"class":css})