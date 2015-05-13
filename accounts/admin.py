from django.contrib import admin
from .models import profile, PersonalMessage


class profileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name')


class PersonalMessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'recipient', 'text', 'send_date')


# register your models with the admin section
admin.site.register(profile, profileAdmin)
admin.site.register(PersonalMessage, PersonalMessageAdmin)
