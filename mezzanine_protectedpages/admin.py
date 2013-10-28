"""
Register the protectedpage content type with the admin backend.
"""
from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from .models import ProtectedPage

admin.site.register(ProtectedPage, PageAdmin)
