from django.shortcuts import redirect, render, render_to_response
from django.http import Http404, HttpResponse, HttpResponseNotFound, QueryDict
from django.utils import simplejson
from models import *
from base64 import b64decode
from django.core.files.base import ContentFile

def add_others(request):
	name = request.GET.get('others_name', "")
	latitude = request.GET.get("latitude", "")
	longitude = request.GET.get("longitude", "")
	others = request.GET.get("others_type", "")
	image = request.GET.get('others_image', None)
	uuid = request.GET.get("uuid", None)
	if image:
		image_data = b64decode(image)
		image_field = ContentFile(image_data, name+'.png')
	else:
		image_field = None
	try:
		temp = Others(name = name, image = image_field, latitude=latitude,
		longitude = longitude, others = others, uuid = uuid)
		temp.save()
	except Exception as e:
		return HttpResponse(e)
		
	
	return HttpResponse(temp.id)

def add_school(request):
	name = request.GET.get('name', "")
	address = request.GET.get("address", "")
	examination_board = request.GET.get("examination_board", "") 
	highest_class = request.GET.get("highest_class", None) 
	latitude = request.GET.get("latitude", "")
	longitude = request.GET.get("longitude", "")
	lowest_class = request.GET.get("lowest_class", None)
	medium_of_instruction = request.GET.get("medium_of_instruction", "")
	monthly_fee_for_highest_class = request.GET.get("monthly_fee_for_highest_class", "")
	monthly_fee_for_lowest_class = request.GET.get("monthly_fee_for_lowest_class", "")
	other_fee_per_annum = request.GET.get("other_fee_per_annum", "")
	pincode = request.GET.get("pincode", 0)
	recognized = request.GET.get("recognized", None)
	school_type = request.GET.get("school_type", None)
	short_name = request.GET.get("short_name", "")
	name_of_personality_1 = request.GET.get("name_of_personality_1", None)
	designation_1 = request.GET.get("designation_1", None) 
	organization_affiliation_1 = request.GET.get("organization_affiliation_1", None) 
	image = request.GET.get('image', None)
	website = request.GET.get("website", None)
	phone_number = request.GET.get("phone_number", None)
	uuid = request.GET.get("uuid", None)
	if image:
		image_data = b64decode(image)
		image_field = ContentFile(image_data, name+'.png')
	else:
		image_field = None
	try:
		temp = School(name = name, address = address, examination_board = examination_board, highest_class = highest_class,
		lowest_class = lowest_class, medium_of_instruction = medium_of_instruction, monthly_fee_for_highest_class = monthly_fee_for_highest_class,
		monthly_fee_for_lowest_class = monthly_fee_for_lowest_class, other_fee_per_annum = other_fee_per_annum, pincode = pincode,
		recognized = recognized, school_type = school_type, short_name = short_name, image = image_field, latitude=latitude,
		longitude = longitude,name_of_personality_1 = name_of_personality_1, designation_1 = designation_1, organization_affiliation_1=organization_affiliation_1,
		website = website, phone_number = phone_number, uuid = uuid)
		temp.save()
	except Exception as e:
		return HttpResponse(e)
		
	
	return HttpResponse(temp.id)

def add_heg(request):
	name = request.GET.get('name', "")
	medium_of_instruction = request.GET.get("medium_of_instruction", "")
	founded_in = request.GET.get("founded_in", "")
	management_type = request.get("management_type", "")
	course_type = request.GET.get("course_type", "")
	main_unaided_courses = request.GET.get("main_unaided_courses", "") 
	name_of_the_trust = request.GET.get("name_of_the_trust", None)
	name_of_personality_1 = request.GET.get("name_of_personality_1", None)
	designation_1 = request.GET.get("designation_1", None) 
	organization_affiliation_1 = request.GET.get("organization_affiliation_1", None) 
	name_of_personality_2 = request.GET.get("name_of_personality_2", None) 
	designation_2 = request.GET.get("designation_2", None)
	organization_affiliation_2 = request.GET.get("organization_affiliation_2", None)
	latitude = request.GET.get("latitude", "")
	longitude = request.GET.get("longitude", "")
	website = request.GET.get("website", None)
	phone_number = request.GET.get("phone_number", None)
	image = request.GET.get('heg_image', None)
	uuid = request.GET.get("uuid", None)
	if image:
		image_data = b64decode(image)
		image_field = ContentFile(image_data, name+'.png')
	else:
		image_field = None
	try:
		temp = HEGForm(name = name, medium_of_instruction = medium_of_instruction, founded_in = founded_in, management_type = management_type,
		course_type = course_type, main_unaided_courses = main_unaided_courses, name_of_the_trust = name_of_the_trust,
		name_of_personality_1 = name_of_personality_1, designation_1 = designation_1, organization_affiliation_1 = organization_affiliation_1,
		name_of_personality_2 = name_of_personality_2, designation_2 = designation_2, organization_affiliation_2 = organization_affiliation_2, 
		website = website, phone_number = phone_number, image = image_field, latitude=latitude, longitude = longitude, uuid = uuid)
		temp.save()
	except Exception as e:
		return HttpResponse(e)
		
	
	return HttpResponse(temp.id)

def tastypie_post(request):
    return render_to_response('tastypie_post.html')
