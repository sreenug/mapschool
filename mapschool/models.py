from django.db import models

class School(models.Model):
    CLASS_CHOICES = (
        (1, 'First'),
        (2, 'Second'),
        (3, 'Third'),
        (4, 'Fourth'),
        (5, 'Fifth'),
        (6, 'Sixth'),
        (7, 'Seventh'),
        (8, 'Eight'),
        (9, 'Ninth'),
        (10, 'Tenth'),
        (11, 'Eleventh'),
        (12, 'Twelth'),
    )
    RECOGNIZED_CHOICES = (
        (1, 'Yes'),
        (0, 'No'),
    )
    TYPE_CHOICES = (
        (1, 'Government Aided'),
        (0, 'Private'),
        (2, 'Goverenment'),
        (3, 'Religious'),
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
        ('CISE','CISE'),
        ('CBSE','CBSE'),
        ('State board','State board'),
        ('Foreign board','Foreign board'),
        ('Not available','Not available'),
        ('Not applicable','Not applicable'),
        ('Other','Other'),
    )
    ORGANIZATION_CHOICES = (
        ('1', 'Government'),
        ('2', 'Congress'),
        ('3', 'BJP'),
        ('4', 'JD(U)'),
        ('5', 'TDP'),
        ('6', 'CPI(M)'),
        ('7', 'MIM'),
        ('8', 'TRS'),
        ('9', 'JD(S)'),
        ('10', 'Independent'),
        ('11', 'Other')
     )
    name = models.CharField(max_length=200)
    lowest_class = models.IntegerField(max_length=2, choices=CLASS_CHOICES)
    highest_class = models.IntegerField(max_length=2, choices=CLASS_CHOICES)
    recognized = models.IntegerField(max_length=2, choices=RECOGNIZED_CHOICES)
    school_type = models.IntegerField(max_length=2, choices=TYPE_CHOICES)
    medium_of_instruction = models.CharField(max_length=200, choices=LANGUAGE_CHOICES)
    pincode = models.IntegerField(max_length=6)
    short_name = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    address_1 = models.CharField(max_length=200, blank=True, null=True)
    address_2 = models.CharField(max_length=200, blank=True, null=True)
    address_3 = models.CharField(max_length=200, blank=True, null=True)
    address_4 = models.CharField(max_length=200, blank=True, null=True)
    address_5 = models.CharField(max_length=200, blank=True, null=True)
    examination_board = models.CharField(max_length=100, choices=BOARD_CHOICES)
    other_fee_per_annum = models.CharField(max_length=50, blank=True)
    monthly_fee_for_lowest_class = models.CharField(max_length=50, blank=True)
    monthly_fee_for_highest_class = models.CharField(max_length=50, blank=True)
    name_of_personality_1 = models.CharField(max_length=200,blank=True, null=True)
    designation_1 = models.CharField(max_length=200,blank=True, null=True)
    organization_affiliation_1 = models.CharField(max_length=200,blank=True, null=True, choices=ORGANIZATION_CHOICES)
    latitude = models.CharField(max_length=20, blank = True, null=True)
    longitude = models.CharField(max_length=20, blank = True, null=True)
    website = models.CharField(max_length=200, blank = True, null=True)
    phone_number = models.CharField(max_length=200, blank = True, null=True)
    uuid = models.CharField(max_length=100, blank = True, null=True)
    image= models.ImageField(upload_to='mapschool/mapschool/images', blank=True,null=True)
    
    class Meta:
        db_table = u'school'
        
    def __unicode__(self):
        return self.name

class HEGForm(models.Model):
    CLASS_CHOICES = (
        ('1', 'Medicine'),
        ('2', 'Engineering'),
        ('3', 'Management-MBA'),
        ('4', 'Diploma-Engineering'),
        ('5', 'Bed/Teacher Training'),
        ('6', 'Dental'),
        ('7', 'Paramedical'),
        ('8', 'Other Professional Course(s)'),
        ('9', 'Other'),
        )
    ORGANIZATION_CHOICES = (
        ('1', 'Government'),
        ('2', 'Congress'),
        ('3', 'BJP'),
        ('4', 'JD(U)'),
        ('5', 'TDP'),
        ('6', 'CPI(M)'),
        ('7', 'MIM'),
        ('8', 'TRS'),
        ('9', 'JD(S)'),
        ('10', 'Independent'),
        ('11', 'Other')
     )
    
    RECOGNIZED_CHOICES = (
        (1, 'Yes'),
        (0, 'No'),
    )
    TYPE_CHOICES = (
        (1, 'University'),
        (2, 'AIDED COLLEGE'),
        (3, 'UNAIDED COLLEGE'),        
    )
    LANGUAGE_CHOICES = (
        ('English','English'),
        ('Hindi','Hindi'),
        ('Mix English and Hindi','Mix English and Hindi'),
        ('Urdu','Urdu'),
        ('Gujrathi','Gujrathi'),
        ('Tamil','Tamil'),
        ('Telugu','Telugu'),
        ('Punjabi','Punjabi'),
        ('Malayalam','Malayalam'),
        ('Marathi','Marathi'),
        ('Bengali','Bengali'),
        ('Oriya','Oriya'),
        ('Assamese','Assamese'),
        ('Other','Other'),
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
    name = models.CharField(max_length=200)
    medium_of_instruction = models.CharField(max_length=200, choices=LANGUAGE_CHOICES)
    founded_in = models.DateField(null=True, db_column='founded_in', blank=True)
    management_type = models.IntegerField(max_length=2, choices=TYPE_CHOICES)
    course_type = models.CharField(max_length = 200, choices=COURSE_TYPE_CHOICES)
    main_unaided_courses = models.CharField(max_length = 200, choices=CLASS_CHOICES)
    name_of_the_trust = models.CharField(max_length=200)
    name_of_personality_1 = models.CharField(max_length=200,blank=True, null=True)
    designation_1 = models.CharField(max_length=200,blank=True, null=True)
    organization_affiliation_1 = models.CharField(max_length=200,blank=True, null=True, choices=ORGANIZATION_CHOICES)
    name_of_personality_2 = models.CharField(max_length=200,blank=True, null=True)
    designation_2 = models.CharField(max_length=200,blank=True, null=True)
    organization_affiliation_2 = models.CharField(max_length=200,blank=True, null=True, choices=ORGANIZATION_CHOICES)
    address = models.CharField(max_length=200, blank=True, null=True)
    address_1 = models.CharField(max_length=200, blank=True, null=True)
    address_2 = models.CharField(max_length=200, blank=True, null=True)
    address_3 = models.CharField(max_length=200, blank=True, null=True)
    address_4 = models.CharField(max_length=200, blank=True, null=True)
    address_5 = models.CharField(max_length=200, blank=True, null=True)
    latitude = models.CharField(max_length=20, blank = True, null=True)
    longitude = models.CharField(max_length=20, blank = True, null=True)
    website = models.CharField(max_length=200, blank = True, null=True)
    phone_number = models.CharField(max_length=200, blank = True, null=True)
    uuid = models.CharField(max_length=100, blank = True, null=True)
    image= models.ImageField(upload_to='mapschool/mapschool/images/heg', blank=True,null=True)
    class Meta:
        db_table = u'heg_form'
        
    def __unicode__(self):
        return self.name

class Others(models.Model):
    
    OTHER_CHOICES = (
        ('Busstop','Busstop'),
        ('Railway Station','Railway Station'),
        ('Autostand','Autostand'),
        ('Temple','Temple'),        
    )
    others = models.CharField(max_length=200,blank=True, null=True, choices=OTHER_CHOICES)
    name = models.CharField(max_length=200)
    latitude = models.CharField(max_length=20, blank = True, null=True)
    longitude = models.CharField(max_length=20, blank = True, null=True)
    image= models.ImageField(upload_to='mapschool/mapschool/images/others', blank=True,null=True)
    uuid = models.CharField(max_length=100, blank = True, null=True)
    class Meta:
        db_table = u'others'
        
    def __unicode__(self):
        return self.name