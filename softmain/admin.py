from django.contrib import admin
from .models import Email

class EmailAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject']


admin.site.register(Email, EmailAdmin)
