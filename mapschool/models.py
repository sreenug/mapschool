from django.db import models

#Choice fields
CLASS_CHOICES = (
    ('First', 'First'),
    ('Second', 'Second'),
    ('Third', 'Third'),
    ('Fourth', 'Fourth'),
    ('Fifth', 'Fifth'),
    ('Sixth', 'Sixth'),
    ('Seventh', 'Seventh'),
    ('Eigth', 'Eigth'),
    ('Ninth', 'Ninth'),
    ('Tenth', 'Tenth'),
    ('Eleventh', 'Eleventh'),
    ('Twelth', 'Twelth'),
)
RECOGNIZED_CHOICES = (
    ('Yes', 'Yes'),
    ('No', 'No'),
)
TYPE_CHOICES = (
    ('Government Aided', 'Government Aided'),
    ('Private', 'Private'),
    ('Government', 'Government'),
    ('Religious', 'Religious'),
    ('Special School', 'Special School'),
)
LANGUAGE_CHOICES = (
    ('English','English'),
    ('Hindi','Hindi'),
    ('Mix English and Hindi','Mix English and Hindi'),
    ('Urdu','Urdu'),
    ('Gujarati','Gujarati'),
    ('Tamil','Tamil'),
    ('Telugu','Telugu'),
    ('Kannad','Kannad'),
    ('Punjabi','Punjabi'),
    ('Malayalam','Malayalam'),
    ('Marathi','Marathi'),
    ('Bengali','Bengali'),
    ('Oriya','Oriya'),
    ('Assamese','Assamese'),
    ('Other','Other'),
)
BOARD_CHOICES = (
    ('CISCE','CISCE'),
    ('CBSE','CBSE'),
    ('State board','State board'),
    ('Foreign board','Foreign board'),
    ('Not available','Not available'),
    ('Not applicable','Not applicable'),
    ('Other','Other'),
)
GENDER_CHOICES = (
    ('Girls','Only Girls'),
    ('Boys','Only Boys'),
    ('Co Education','Co Education'),        
)
ORGANIZATION_CHOICES = (
    ('Government', 'Government'),
    ('Congress', 'Congress'),
    ('BJP', 'BJP'),
    ('JD(U)', 'JD(U)'),
    ('TDP', 'TDP'),
    ('CPI(M)', 'CPI(M)'),
    ('MIM', 'MIM'),
    ('TRS', 'TRS'),
    ('JD(S)', 'JD(S)'),
    ('Independent', 'Independent'),
    ('Other', 'Other')
)
    
###For Hei Form
HEI_CLASS_CHOICES = (
    ('Medicine', 'Medicine'),
    ('Engineering', 'Engineering'),
    ('Management-MBA', 'Management-MBA'),
    ('Management-BBA', 'Management-BBA'),
    ('Diploma-Engineering', 'Diploma-Engineering'),
    ('BEd/Teacher Training', 'BEd/Teacher Training'),
    ('Dentistry', 'Dentistry'),
    ('Paramedical', 'Paramedical'),
    ('Other Professional Course(s)', 'Other Professional Course(s)'),
    ('Other', 'Other'),
)
HEI_TYPE_CHOICES = (
    ('University', 'University'),
    ('Aided College', 'Aided College'),
    ('Unaided College', 'Unaided College')        
)
COURSE_TYPE_CHOICES = (
    ('ASC','ASC'),
    ('Engg./Tech./Arch./Management','Engg./Tech./Arch./Management'),
    ('Medical','Medical'),
    ('Law','Law'),
    ('Teacher Edu','Teacher Edu'),
    ('Polytechnic','Polytechnic'),
    ('Diploma','Diploma'),
    ('Agriculture','Agriculture'),
    ('Other','Other'),
)

###For Other Form
OTHER_CHOICES = (
    ('Busstop','Busstop'),
    ('Railway Station','Railway Station'),
    ('Autostand','Autostand'),
    ('Temple','Temple'),
	('Other', 'Other')
)
class School(models.Model):
    name = models.CharField(max_length=200)
    lowest_class = models.CharField(max_length=200, choices=CLASS_CHOICES)
    highest_class = models.CharField(max_length=200, choices=CLASS_CHOICES)
    recognized = models.CharField(max_length=10, choices=RECOGNIZED_CHOICES)
    management_type = models.CharField(max_length=100, choices=TYPE_CHOICES)
    gender_type = models.CharField(max_length=100, choices=GENDER_CHOICES)
    medium_of_instruction = models.CharField(max_length=100, choices=LANGUAGE_CHOICES)
    medium_of_instruction_other = models.CharField(max_length=100, null=True, blank=True)
    examination_board = models.CharField(max_length=100, choices=BOARD_CHOICES)
    examination_board_other = models.CharField(max_length=100, null=True, blank=True)
    short_name = models.CharField(max_length=50, blank=True, null=True)
    preschool_attached = models.CharField(max_length=10, choices=RECOGNIZED_CHOICES, blank=True, null=True)
    preschool_attached_name = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    address_1 = models.CharField(max_length=100, blank=True, null=True)
    address_2 = models.CharField(max_length=100, blank=True, null=True)
    address_3 = models.CharField(max_length=100, blank=True, null=True)
    address_4 = models.CharField(max_length=100, blank=True, null=True)
    address_5 = models.CharField(max_length=100, blank=True, null=True)
    pincode = models.IntegerField(max_length=6, null=True, blank=True)
    monthly_fee_for_lowest_class = models.CharField(max_length=50, null=True, blank=True)
    monthly_fee_for_highest_class = models.CharField(max_length=50, null=True, blank=True)
    other_fee_per_annum = models.CharField(max_length=200, null=True, blank=True)
    name_of_personality_1 = models.CharField(max_length=200,blank=True, null=True)
    designation_1 = models.CharField(max_length=200,blank=True, null=True)
    organization_affiliation_1 = models.CharField(max_length=100,blank=True, null=True, choices=ORGANIZATION_CHOICES)
    organization_affiliation_1_other = models.CharField(max_length=100,blank=True, null=True)
    name_of_personality_2 = models.CharField(max_length=200,blank=True, null=True)
    designation_2 = models.CharField(max_length=200,blank=True, null=True)
    organization_affiliation_2 = models.CharField(max_length=100,blank=True, null=True, choices=ORGANIZATION_CHOICES)
    organization_affiliation_2_other = models.CharField(max_length=100,blank=True, null=True)
    name_of_personality_3 = models.CharField(max_length=200,blank=True, null=True)
    designation_3 = models.CharField(max_length=200,blank=True, null=True)
    organization_affiliation_3 = models.CharField(max_length=100,blank=True, null=True, choices=ORGANIZATION_CHOICES)
    organization_affiliation_3_other = models.CharField(max_length=100,blank=True, null=True)
    latitude = models.CharField(max_length=20, blank = True, null=True)
    longitude = models.CharField(max_length=20, blank = True, null=True)
    website = models.CharField(max_length=200, blank = True, null=True)
    phone_number = models.CharField(max_length=200, blank = True, null=True)
    uuid = models.CharField(max_length=100, blank = True, null=True)
    image= models.ImageField(upload_to='mapschool/mapschool/images', blank=True,null=True)
    time_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    time_modified = models.DateTimeField(auto_now=True, null=True, blank=True)
    
    class Meta:
        db_table = u'school'
        
    def __unicode__(self):
        return self.name

class HEIForm(models.Model):
    name = models.CharField(max_length=200)
    medium_of_instruction = models.CharField(max_length=100, choices=LANGUAGE_CHOICES)
    medium_of_instruction_other = models.CharField(max_length=200, null=True, blank=True)
    founded_in = models.DateField(null=True, db_column='founded_in', blank=True)
    management_type = models.CharField(max_length=100, choices=HEI_TYPE_CHOICES)
    course_type_1 = models.CharField(max_length = 100, choices=COURSE_TYPE_CHOICES)
    course_type_2 = models.CharField(max_length = 100, choices=COURSE_TYPE_CHOICES, null=True, blank=True)
    course_type_3 = models.CharField(max_length = 100, choices=COURSE_TYPE_CHOICES, null=True, blank=True)
    course_type_4 = models.CharField(max_length = 100, choices=COURSE_TYPE_CHOICES, null=True, blank=True)
    course_type_5 = models.CharField(max_length = 100, choices=COURSE_TYPE_CHOICES, null=True, blank=True)
    main_unaided_courses = models.CharField(max_length = 200, choices=HEI_CLASS_CHOICES, null=True, blank=True)
    main_unaided_courses_other = models.CharField(max_length = 200, null=True, blank=True)
    name_of_the_trust = models.CharField(max_length=200)
    name_of_personality_1 = models.CharField(max_length=200,blank=True, null=True)
    designation_1 = models.CharField(max_length=200,blank=True, null=True)
    organization_affiliation_1 = models.CharField(max_length=200,blank=True, null=True, choices=ORGANIZATION_CHOICES)
    organization_affiliation_1_other = models.CharField(max_length=100,blank=True, null=True)
    name_of_personality_2 = models.CharField(max_length=200,blank=True, null=True)
    designation_2 = models.CharField(max_length=200,blank=True, null=True)
    organization_affiliation_2 = models.CharField(max_length=200,blank=True, null=True, choices=ORGANIZATION_CHOICES)
    organization_affiliation_2_other = models.CharField(max_length=100,blank=True, null=True)
    name_of_personality_3 = models.CharField(max_length=200,blank=True, null=True)
    designation_3 = models.CharField(max_length=200,blank=True, null=True)
    organization_affiliation_3 = models.CharField(max_length=200,blank=True, null=True, choices=ORGANIZATION_CHOICES)
    organization_affiliation_3_other = models.CharField(max_length=100,blank=True, null=True)
    name_of_personality_4 = models.CharField(max_length=200,blank=True, null=True)
    designation_4 = models.CharField(max_length=200,blank=True, null=True)
    organization_affiliation_4 = models.CharField(max_length=200,blank=True, null=True, choices=ORGANIZATION_CHOICES)
    organization_affiliation_4_other = models.CharField(max_length=100,blank=True, null=True)
    name_of_personality_5 = models.CharField(max_length=200,blank=True, null=True)
    designation_5 = models.CharField(max_length=200,blank=True, null=True)
    organization_affiliation_5 = models.CharField(max_length=200,blank=True, null=True, choices=ORGANIZATION_CHOICES)
    organization_affiliation_5_other = models.CharField(max_length=100,blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    address_1 = models.CharField(max_length=200, blank=True, null=True)
    address_2 = models.CharField(max_length=200, blank=True, null=True)
    address_3 = models.CharField(max_length=200, blank=True, null=True)
    address_4 = models.CharField(max_length=200, blank=True, null=True)
    address_5 = models.CharField(max_length=200, blank=True, null=True)
    pincode = models.IntegerField(max_length=6, null=True, blank=True)
    latitude = models.CharField(max_length=20, blank = True, null=True)
    longitude = models.CharField(max_length=20, blank = True, null=True)
    website = models.CharField(max_length=200, blank = True, null=True)
    phone_number = models.CharField(max_length=200, blank = True, null=True)
    uuid = models.CharField(max_length=100, blank = True, null=True)
    image= models.ImageField(upload_to='mapschool/mapschool/images/heg', blank=True,null=True)
    time_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    time_modified = models.DateTimeField(auto_now=True, null=True, blank=True)
    
    class Meta:
        db_table = u'hei_form'
        
    def __unicode__(self):
        return self.name

class Other(models.Model):
    others = models.CharField(max_length=200,blank=True, null=True, choices=OTHER_CHOICES)
    others_others = models.CharField(max_length=200,blank=True, null=True)
    name = models.CharField(max_length=200)
    latitude = models.CharField(max_length=20, blank = True, null=True)
    longitude = models.CharField(max_length=20, blank = True, null=True)
    image= models.ImageField(upload_to='mapschool/mapschool/images/others', blank=True,null=True)
    uuid = models.CharField(max_length=100, blank = True, null=True)
    time_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    time_modified = models.DateTimeField(auto_now=True, null=True, blank=True)
    
    class Meta:
        db_table = u'others'
        
    def __unicode__(self):
        return self.name