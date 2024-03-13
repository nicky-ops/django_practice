from django.contrib import admin
from .models import SearchKeyword
from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.admin import FlatPageAdmin
# Register your models here.

class SearchKeywordInline(admin.StackedInline):
    model = SearchKeyword

class FlatPageAdminWithKeywords(FlatPageAdmin):
    inlines = [SearchKeywordInline]

admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdminWithKeywords)