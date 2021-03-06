from django.contrib import admin

# Register your models here.
from models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ('account',)
    list_filter = ('time',)


class ResumeAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'language', 'is_open')
    list_filter = ('language',)
    search_fields = ('title',)


class StyleAdmin(admin.ModelAdmin):
    list_display = ('info', 'css_addr')


class IDMapAdmin(admin.ModelAdmin):
    list_display = ('openid', 'name')


admin.site.register(User, UserAdmin)
admin.site.register(Resume, ResumeAdmin)
admin.site.register(Style, StyleAdmin)
admin.site.register(IDMap, IDMapAdmin)
