from django.contrib import admin
from .models import Contacts, SocialMedia, ContactWithUs, FAQ


# Register your models here.

class ContactsAdmin(admin.ModelAdmin):
    list_display = ["id", "phone_number"]
    list_editable = ["phone_number"]


class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ["id", "telegram"]
    list_display_links = ["id", "telegram"]


class ContactWithUsAdmin(admin.ModelAdmin):
    list_display = ["id", "phone_number", "message"]
    search_fields = ["phone_number"]


class FAQAdmin(admin.ModelAdmin):
    list_display = ["id", "question", "answer"]


admin.site.register(Contacts, ContactsAdmin)
admin.site.register(SocialMedia, SocialMediaAdmin)
admin.site.register(ContactWithUs, ContactWithUsAdmin)
admin.site.register(FAQ, FAQAdmin)
