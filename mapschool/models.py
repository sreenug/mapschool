from django.db import models

class Language(models.Model):
    language_name = models.CharField(max_length=100,  unique='True')
    class Meta:
        db_table = u'language'

    def __unicode__(self):
        return self.language_name

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
        (1, 'YES'),
        (0, 'No'),
    )
    TYPE_CHOICES = (
        (1, 'Goverenment Aided'),
        (0, 'Private'),
        (2, 'Goverenment'),
        (3, 'Religious'),
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
    name = models.CharField(max_length=200)
    lowest_class = models.IntegerField(max_length=2, choices=CLASS_CHOICES)
    highest_class = models.IntegerField(max_length=2, choices=CLASS_CHOICES)
    recognized = models.IntegerField(max_length=2, choices=RECOGNIZED_CHOICES)
    type = models.IntegerField(max_length=2, choices=TYPE_CHOICES)
    medium_of_instructions = models.ForeignKey(Language, verbose_name='Medium Of Instruction', null=True, blank=True)
    pincode = models.IntegerField(max_length=6)
    short_name = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=200, blank=True)
    examination_board = models.CharField(max_length=100, blank=True)
    other_fee_per_annum = models.CharField(max_length=50, blank=True)
    monthly_fee_for_lowest_class = models.CharField(max_length=50, blank=True)
    monthly_fee_for_highest_class = models.CharField(max_length=50, blank=True)
    
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
        ('9', 'Independent'),
        ('10', 'Other')
     )
    
    RECOGNIZED_CHOICES = (
        (1, 'YES'),
        (0, 'No'),
    )
    TYPE_CHOICES = (
        ('University', 'University'),
        ('College-Professional', 'College-Professional'),
        ('College-General Degree', 'College-General Degree'),
        ('College-Diploma', 'College-Diploma'),
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
    name = models.CharField(max_length=200)
    founded_in = models.DateField(null=True, db_column='founded_in', blank=True)
    type = models.IntegerField(max_length=2, choices=TYPE_CHOICES)
    main_unaided_courses = models.CharField(max_length = 200, choices=CLASS_CHOICES)
    name_of_the_trust = models.CharField(max_length=200)
    name_of_personality_1 = models.CharField(max_length=200,blank=True, null=True)
    designation_1 = models.CharField(max_length=200,blank=True, null=True)
    organization_affiliation_1 = models.CharField(max_length=200,blank=True, null=True, choices=ORGANIZATION_CHOICES)
    name_of_personality_2 = models.CharField(max_length=200,blank=True, null=True)
    designation_2 = models.CharField(max_length=200,blank=True, null=True)
    organization_affiliation_2 = models.CharField(max_length=200,blank=True, null=True, choices=ORGANIZATION_CHOICES)
    
    class Meta:
        db_table = u'heg_form'
        
    def __unicode__(self):
        return self.name