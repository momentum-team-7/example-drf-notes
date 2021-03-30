from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Note, User, Tag

admin.site.register(Note)
admin.site.register(Tag)
admin.site.register(User, UserAdmin)
