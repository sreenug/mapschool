from django.contrib import admin
from models import *

class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'place_name')
    search_fields = ['name', 'place_name']

class OthersAdmin(admin.ModelAdmin):
    list_display = ('name', 'others')
    search_fields = ['name', 'others']


class HEIFormAdmin(admin.ModelAdmin):
    list_display = ('name', 'founded_in', 'name_of_the_trust', 'name_of_personality_1', 'name_of_personality_2')
    search_fields = ['name', 'founded_in', 'name_of_the_trust', 'name_of_personality_1', 'name_of_personality_1']

admin.site.register(School, SchoolAdmin)
admin.site.register(HEIForm, HEIFormAdmin)
admin.site.register(Other, OthersAdmin)
