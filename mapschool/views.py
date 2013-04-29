from django.shortcuts import redirect, render, render_to_response
from django.http import Http404, HttpResponse, HttpResponseNotFound, QueryDict
from django.utils import simplejson

def add_school(request):
    return HttpResponse(simplejson.dumps({"id":"10", "name":"sri"}), mimetype="application/json")

def tastypie_post(request):
    return render_to_response('tastypie_post.html')
