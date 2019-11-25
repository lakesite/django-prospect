from django import forms
from django.contrib import admin
import django.contrib.auth.admin

from prospect.models import (Prospect, Company, ProspectNote, ProspectList)


class ProspectNotesInline(admin.StackedInline):
    model = ProspectNote
    extra = 0


class ProspectInline(admin.StackedInline):
    model = Prospect
    extra = 0


class ProspectListInline(admin.StackedInline):
    model = ProspectList.prospects.through
    extra = 0


class CompanyInline(admin.StackedInline):
    model = Company
    extra = 0


class ProspectAdmin(admin.ModelAdmin):
    inlines = [ProspectNotesInline,]


class ProspectListAdmin(admin.ModelAdmin):
    inlines = [ProspectListInline,]
    exclude = ('prospects',)


class CompanyAdmin(admin.ModelAdmin):
    inlines = [ProspectInline,]


admin.site.register(Prospect, ProspectAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(ProspectList, ProspectListAdmin)
