from django.contrib import admin
from .models import *
from django import forms


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'date_check', 'company', 'special')
    list_display_links = ('full_name', 'date_check', 'company', 'special')
    list_filter = ('reason', 'previous_date_eb', )
    search_fields = ('full_name', )
    autocomplete_fields = ('company', )


class SpecialAdmin(admin.ModelAdmin):
    list_display = ('post', 'group_eb',)
    list_display_links = ('post', 'group_eb',)
    list_filter = ('post', 'group_eb', )
    search_fields = ('post', )


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)
    autocomplete_fields = ('specials', )


class PersonAdmin(admin.ModelAdmin):
    list_display = ('username',)
    list_display_links = ('username',)
    list_filter = ('username', 'is_staff', 'is_superuser')
    search_fields = ('username',)
    autocomplete_fields = ('company',)


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Special, SpecialAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Person, PersonAdmin)
