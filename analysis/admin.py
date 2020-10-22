from django.contrib import admin
from .models import Company, Statement
# Register your models here.

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
  list_display = ('name',)
  list_display_links = ('name',)

@admin.register(Statement)
class StatementAdmin(admin.ModelAdmin):
  list_display = ('company', 'fiscal_year')
  list_display_links = ('company',)
