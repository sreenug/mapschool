from django.shortcuts import redirect, render, render_to_response
from django.http import Http404, HttpResponse, HttpResponseNotFound, QueryDict

def add_school(request):
    return HttpResponse('success')

def tastypie_post(request):
    return render_to_response('tastypie_post.html')
