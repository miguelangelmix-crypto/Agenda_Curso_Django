from django.contrib import admin

# Register your models here.
from contact import models

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )
    ordering = ('-id',)
  
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone', )
    search_fields = ('id', 'first_name', 'last_name')
    #list_filter = ('created_date',)
    ordering = ('-id',)
    list_per_page = 10
    list_max_show_all=50
    list_editable = ('phone',)
    list_display_links = ('id', 'first_name', 'last_name',)

    