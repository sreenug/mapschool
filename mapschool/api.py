from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from mapschool.models import School


class SchoolResource(ModelResource):
    class Meta:
        queryset = School.objects.all()
        resource_name = 'school'
        authorization= Authorization()