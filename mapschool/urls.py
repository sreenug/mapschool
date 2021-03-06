from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
from api import SchoolResource
import views
school_resource = SchoolResource()

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mapschool.views.home', name='home'),
    # url(r'^mapschool/', include('mapschool.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(school_resource.urls)),
    url(r'^addschool/', views.add_school),
	url(r'^addothers/', views.add_others),
	url(r'^addheg/', views.add_heg),
	url(r'^tastypie/post/?$',views.tastypie_post),
	url(r'^getschool/', views.get_school),
	url(r'^search/', views.search),
)
