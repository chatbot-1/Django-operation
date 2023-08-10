from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(ContactUs)
admin.site.register(Popular)
admin.site.register(Regular)