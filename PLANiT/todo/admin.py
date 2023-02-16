from django.contrib import admin
from .models import *

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'creator', 'complete')

class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'creator', 'join_link')

class MembershipAdmin(admin.ModelAdmin):
    list_display = ('group', 'user', 'join_token')

# Register your models here.
admin.site.register(Task, TaskAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Membership, MembershipAdmin)
