from django.contrib import admin
from models import *

class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'lowest_class', 'highest_class', 'medium_of_instructions')
    search_fields = ['name', 'pincode', 'medium_of_instructions']

admin.site.register(Language)
admin.site.register(School, SchoolAdmin)
