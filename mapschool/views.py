from django.shortcuts import redirect, render, render_to_response
def add_school(request):
    return render_to_response('add_school.html')

def tastypie_post(request):
    return render_to_response('tastypie_post.html')
