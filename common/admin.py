from django.contrib import admin
from .models import *

from django.contrib.auth.models import User, Group

admin.site.unregister(User)
admin.site.unregister(Group)


class MediaAdmin(admin.ModelAdmin):
    list_display = ["id", "type"]
    list_filter = ["type"]


admin.site.register(Media, MediaAdmin)
