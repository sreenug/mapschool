from django.shortcuts import redirect, render, render_to_response
from django.http import Http404, HttpResponse, HttpResponseNotFound, QueryDict
from django.utils import simplejson
from models import *
from base64 import b64decode
from django.core.files.base import ContentFile
from urlparse import parse_qs


def add_others(request):
    qs_string = parse_qs(request.GET.get('form_data'))
    name = qs_string.get('name', [None])
    latitude = request.GET.get("latitude", None)
    longitude = request.GET.get("longitude", None)
    others = qs_string.get("others_type", [None])
    others_others = qs_string.get("others_others", [None])
    image = request.GET.get('others_image', None)
    uuid = request.GET.get("uuid", None)
    if image:
        image_data = b64decode(image)
        image_field = ContentFile(image_data, name[0]+'.png')
    else:
        image_field = None
    try:
        temp = Other(name = name[0], image = image_field, latitude=latitude,
        longitude = longitude, others = others[0],others_others = others_others[0], uuid = uuid)
        temp.save()
    except Exception as e:
        return HttpResponse(e)
        
    
    return HttpResponse(temp.id)

def add_school(request):
    qs_string = parse_qs(request.GET.get('form_data'))
    print qs_string['name']
    print qs_string.get('name', [None])
    name = qs_string.get('name', [None])
    lowest_class = qs_string.get("lowest_class", [None])
    highest_class = qs_string.get("highest_class", [None]) 
    recognized = qs_string.get("recognized", [None])
    management_type = qs_string.get("management_type", [None])
    gender_type = qs_string.get("gender_type", [None])
    medium_of_instruction = qs_string.get("medium_of_instruction", [None])
    medium_of_instruction_other = qs_string.get("medium_of_instruction_other", [None])
    examination_board = qs_string.get("examination_board", [None]) 
    examination_board_other = qs_string.get("examination_board_other", [None]) 
    short_name = qs_string.get("short_name", [None])
    preschool_attached = qs_string.get("preschool_attached", [None])
    preschool_attached_name = qs_string.get("preschool_attached_name", [None])
    address = qs_string.get("address", [None])
    pincode = qs_string.get("pincode", [None])
    monthly_fee_for_lowest_class = qs_string.get("monthly_fee_for_lowest_class", [None])
    monthly_fee_for_highest_class = qs_string.get("monthly_fee_for_highest_class", [None])
    other_fee_per_annum = qs_string.get("other_fee_per_annum", [None])
    name_of_personality_1 = qs_string.get("name_of_personality_1", [None])
    designation_1 = qs_string.get("designation_1", [None]) 
    organization_affiliation_1 = qs_string.get("organization_affiliation_1", [None]) 
    organization_affiliation_1_other = qs_string.get("organization_affiliation_1_other", [None]) 
    name_of_personality_2 = qs_string.get("name_of_personality_2", [None])
    designation_2 = qs_string.get("designation_2", [None]) 
    organization_affiliation_2 = qs_string.get("organization_affiliation_2", [None]) 
    organization_affiliation_2_other = qs_string.get("organization_affiliation_2_other", [None]) 
    name_of_personality_3 = qs_string.get("name_of_personality_3", [None])
    designation_3 = qs_string.get("designation_3", [None]) 
    organization_affiliation_3 = qs_string.get("organization_affiliation_3", [None]) 
    organization_affiliation_3_other = qs_string.get("organization_affiliation_3_other", [None]) 
    latitude = request.GET.get("latitude", None)
    longitude = request.GET.get("longitude", None)
    website = qs_string.get("website", [None])
    phone_number = qs_string.get("phone_number", [None])
    uuid = request.GET.get("uuid", None)
    image = request.GET.get('image', None)
    if image:
        image_data = b64decode(image)
        image_field = ContentFile(image_data, name[0]+'.png')
    else:
        image_field = None
    try:
        temp = School(name = name[0], 
        lowest_class = lowest_class[0],
        highest_class = highest_class[0],
        recognized = recognized[0], 
        management_type = management_type[0], 
        gender_type=gender_type[0], 
        medium_of_instruction = medium_of_instruction[0],
        medium_of_instruction_other = medium_of_instruction_other[0],
        examination_board = examination_board[0], 
        examination_board_other = examination_board_other[0],
        short_name = short_name[0], 
        preschool_attached=preschool_attached[0], 
        preschool_attached_name=preschool_attached_name[0], 
        address = address[0], 
        pincode = pincode[0], 
        monthly_fee_for_lowest_class = monthly_fee_for_lowest_class[0], 
        monthly_fee_for_highest_class = monthly_fee_for_highest_class[0],
        other_fee_per_annum = other_fee_per_annum[0],
        name_of_personality_1 = name_of_personality_1[0], 
        designation_1 = designation_1[0], 
        organization_affiliation_1=organization_affiliation_1[0],
        organization_affiliation_1_other=organization_affiliation_1_other[0],
        name_of_personality_2 = name_of_personality_2[0], 
        designation_2 = designation_2[0], 
        organization_affiliation_2=organization_affiliation_2[0],
        organization_affiliation_2_other=organization_affiliation_2_other[0],
        name_of_personality_3 = name_of_personality_3[0], 
        designation_3 = designation_3[0], 
        organization_affiliation_3=organization_affiliation_3[0],
        organization_affiliation_3_other=organization_affiliation_3_other[0],
        latitude=latitude,
        longitude = longitude,
        website = website[0], 
        phone_number = phone_number[0], 
        uuid = uuid, 
        image = image_field
        )
        temp.save()
    except Exception as e:
        return HttpResponse(e)
        
    
    return HttpResponse(temp.id)

def add_heg(request):
    qs_string = parse_qs(request.GET.get('form_data'))
    print qs_string['name']
    print qs_string.get('name', [None])
    name = qs_string.get('name', [None])
    medium_of_instruction = qs_string.get("medium_of_instruction", [None])
    medium_of_instruction_other = qs_string.get("medium_of_instruction_other", [None])
    founded_in = qs_string.get("founded_in", [None])
    management_type = qs_string.get("management_type", [None])
    course_type_1 = qs_string.get("course_type_1", [None])
    course_type_2 = qs_string.get("course_type_2", [None]) 
    course_type_3 = qs_string.get("course_type_3", [None]) 
    course_type_4 = qs_string.get("course_type_4", [None])
    course_type_5 = qs_string.get("course_type_5", [None])
    main_unaided_courses = qs_string.get("main_unaided_courses", [None])
    main_unaided_courses_other = qs_string.get("main_unaided_courses_other", [None])
    name_of_the_trust = qs_string.get("name_of_the_trust", [None])
    name_of_personality_1 = qs_string.get("name_of_personality_1", [None])
    designation_1 = qs_string.get("designation_1", [None]) 
    organization_affiliation_1 = qs_string.get("organization_affiliation_1", [None]) 
    organization_affiliation_1_other = qs_string.get("organization_affiliation_1_other", [None]) 
    name_of_personality_2 = qs_string.get("name_of_personality_2", [None])
    designation_2 = qs_string.get("designation_2", [None]) 
    organization_affiliation_2 = qs_string.get("organization_affiliation_2", [None]) 
    organization_affiliation_2_other = qs_string.get("organization_affiliation_2_other", [None]) 
    name_of_personality_3 = qs_string.get("name_of_personality_3", [None])
    designation_3 = qs_string.get("designation_3", [None]) 
    organization_affiliation_3 = qs_string.get("organization_affiliation_3", [None]) 
    organization_affiliation_3_other = qs_string.get("organization_affiliation_3_other", [None]) 
    name_of_personality_4 = qs_string.get("name_of_personality_4", [None])
    designation_4 = qs_string.get("designation_4", [None]) 
    organization_affiliation_4 = qs_string.get("organization_affiliation_4", [None]) 
    organization_affiliation_4_other = qs_string.get("organization_affiliation_4_other", [None]) 
    name_of_personality_5 = qs_string.get("name_of_personality_5", [None])
    designation_5 = qs_string.get("designation_5", [None]) 
    organization_affiliation_5 = qs_string.get("organization_affiliation_5", [None]) 
    organization_affiliation_5_other = qs_string.get("organization_affiliation_5_other", [None]) 
    address = qs_string.get("address", [None])
    pincode = qs_string.get("pincode", [None])
    latitude = request.GET.get("latitude", None)
    longitude = request.GET.get("longitude", None)
    website = qs_string.get("website", [None])
    phone_number = qs_string.get("phone_number", [None])
    uuid = request.GET.get("uuid", None)
    image = request.GET.get('heg_image', None)
    if image:
        image_data = b64decode(image)
        image_field = ContentFile(image_data, name[0]+'.png')
    else:
        image_field = None
    try:
        temp = HEIForm(name = name[0], 
        medium_of_instruction = medium_of_instruction[0], 
        medium_of_instruction_other = medium_of_instruction_other[0], 
        founded_in = founded_in[0], 
        management_type = management_type[0],
        course_type_1 = course_type_1[0], 
        course_type_2 = course_type_2[0],
        course_type_3 = course_type_3[0],
        course_type_4 = course_type_4[0],
        course_type_5 = course_type_5[0],
        main_unaided_courses = main_unaided_courses[0], 
        main_unaided_courses_other = main_unaided_courses_other[0], 
        name_of_the_trust = name_of_the_trust[0],
        name_of_personality_1 = name_of_personality_1[0], 
        designation_1 = designation_1[0], 
        organization_affiliation_1 = organization_affiliation_1[0],
        organization_affiliation_1_other = organization_affiliation_1_other[0],
        name_of_personality_2 = name_of_personality_2[0], 
        designation_2 = designation_2[0], 
        organization_affiliation_2 = organization_affiliation_2[0], 
        organization_affiliation_2_other = organization_affiliation_2_other[0], 
        name_of_personality_3 = name_of_personality_3[0], 
        designation_3 = designation_3[0], 
        organization_affiliation_3 = organization_affiliation_3[0], 
        organization_affiliation_3_other = organization_affiliation_3_other[0], 
        name_of_personality_4 = name_of_personality_4[0], 
        designation_4 = designation_4[0], 
        organization_affiliation_4 = organization_affiliation_4[0], 
        organization_affiliation_4_other = organization_affiliation_4_other[0], 
        name_of_personality_5 = name_of_personality_5[0], 
        designation_5 = designation_5[0], 
        organization_affiliation_5 = organization_affiliation_5[0], 
        organization_affiliation_5_other = organization_affiliation_5_other[0], 
        address=address[0],
        pincode = pincode[0],
        website = website[0], 
        phone_number = phone_number[0], 
        image = image_field, 
        latitude=latitude, 
        longitude = longitude, 
        uuid = uuid
        )
        temp.save()
    except Exception as e:
        return HttpResponse(e)
        
    
    return HttpResponse(temp.id)

def tastypie_post(request):
    return render_to_response('tastypie_post.html')
