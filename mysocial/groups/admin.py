from django.contrib import admin
from . import models
# Register your models here.

# to access group members from admin interface

class GroupMemberInline(admin.TabularInline):
    model = models.GroupMember

admin.site.register(models.Group)
