from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Contact)
admin.site.register(Popular)
admin.site.register(Regular_blogs)
# admin.site.register(Regular)