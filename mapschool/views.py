from django.shortcuts import redirect, render, render_to_response
from django.http import Http404, HttpResponse, HttpResponseNotFound, QueryDict
from django.utils import simplejson
from models import *
from base64 import b64decode
from django.core.files.base import ContentFile

def add_school(request):
	name = request.GET.get('name', "")
	address = request.GET.get("address", "")
	examination_board = request.GET.get("examination_board", "") 
	highest_class = request.GET.get("highest_class", None) 
	latitude = request.GET.get("latitude", "")
	longitude = request.GET.get("longitude", "")
	lowest_class = request.GET.get("lowest_class", None)
	medium_of_instructions = request.GET.get("medium_of_instructions", "")
	monthly_fee_for_highest_class = request.GET.get("monthly_fee_for_highest_class", "")
	monthly_fee_for_lowest_class = request.GET.get("monthly_fee_for_lowest_class", "")
	other_fee_per_annum = request.GET.get("other_fee_per_annum", "")
	pincode = request.GET.get("pincode", 0)
	recognized = request.GET.get("recognized", None)
	school_type = request.GET.get("school_type", None)
	short_name = request.GET.get("short_name", "")
	image = request.GET.get('image', None)
	if image:
		image_data = b64decode(image)
		image_field = ContentFile(image_data, name+'.png')
	else:
		image_field = None
	try:
		temp = School(name = name, address = address, examination_board = examination_board, highest_class = highest_class,
		lowest_class = lowest_class, medium_of_instructions = medium_of_instructions, monthly_fee_for_highest_class = monthly_fee_for_highest_class,
		monthly_fee_for_lowest_class = monthly_fee_for_lowest_class, other_fee_per_annum = other_fee_per_annum, pincode = pincode,
		recognized = recognized, school_type = school_type, short_name = short_name, image = image_field, latitude=latitude,
		longitude = longitude)
		temp.save()
	except Exception as e:
		return HttpResponse(e)
		
	
	return HttpResponse(temp.id)

def tastypie_post(request):
    return render_to_response('tastypie_post.html')
