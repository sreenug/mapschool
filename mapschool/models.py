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
        (1, 'Goverement Aided'),
        (0, 'Private'),
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
    medium_of_instructions = models.ForeignKey(Language)
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
