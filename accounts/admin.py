from django.contrib import admin

from .models import CustomUser, Direction

admin.site.register([Direction, CustomUser])