from django.contrib import admin
from django.template.defaultfilters import register
from .models import Profile,Relationship
# Register your models here.

admin.site.register(Profile)
admin.site.register(Relationship)