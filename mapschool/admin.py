from django.contrib import admin
from models import *

class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'lowest_class', 'highest_class', 'medium_of_instructions')
    search_fields = ['name', 'pincode', 'medium_of_instructions']

class OthersAdmin(admin.ModelAdmin):
    list_display = ('name', 'others')
    search_fields = ['name', 'others']


class HEGFormAdmin(admin.ModelAdmin):
    fieldsets = [
                (None, {'fields':['name','founded_in', 'type', 'main_unaided_courses', 'name_of_the_trust']}),
                ('Eminent Personality Affiliation',{'fields':['name_of_personality_1','designation_1','organization_affiliation_1',
				'name_of_personality_2','designation_2','organization_affiliation_2']}),                
    ]
    list_display = ('name', 'founded_in', 'name_of_the_trust', 'name_of_personality_1', 'name_of_personality_2')
    search_fields = ['name', 'founded_in', 'name_of_the_trust', 'name_of_personality_1', 'name_of_personality_1']

admin.site.register(School, SchoolAdmin)
admin.site.register(HEGForm, HEGFormAdmin)
admin.site.register(Others, OthersAdmin)
