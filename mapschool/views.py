from django.shortcuts import redirect, render, render_to_response
from django.http import Http404, HttpResponse, HttpResponseNotFound, QueryDict
from django.utils import simplejson

def add_school(request):
	name = request.GET.get('name', "n")
	test = request.GET.get('test', "n")
	rt = name + test
	return HttpResponse(rt)

def tastypie_post(request):
    return render_to_response('tastypie_post.html')
