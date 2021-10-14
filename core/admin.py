from django.contrib import admin
from .models import Shortener, Access

# Register your models here.

admin.site.register(Shortener)
admin.site.register(Access)
