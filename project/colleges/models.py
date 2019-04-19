from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify

# Create your models here.
class CollegeDetails(models.Model):
    name = models.CharField(max_length=200,blank=True)
    slug = models.SlugField(unique=True,max_length=200)
    location = models.CharField(max_length=200,blank=True)
    rating = models.CharField(max_length=20,blank=True)
    placements = models.CharField(max_length=20,blank=True)
    fees = models.CharField(max_length=20,blank=True)
    CS_seats = models.CharField(max_length=20,blank=True)
    IT_seats = models.CharField(max_length=20,blank=True)
    EXTC_seats = models.CharField(max_length=20,blank=True)
    Electrical_seats = models.CharField(max_length=20,blank=True)
    chem_seats = models.CharField(max_length=20,blank=True)
    civil_seats = models.CharField(max_length=20,blank=True)
    mechanical_seats = models.CharField(max_length=20,blank=True)
    electronics_seats = models.CharField(max_length=20,blank=True)
    extra_1 = models.CharField(max_length=200,blank=True)
    extra_2 = models.CharField(max_length=200,blank=True)
    extra_3 = models.CharField(max_length=200,blank=True)
    extra_4 = models.CharField(max_length=200,blank=True)
    description = models.TextField(blank=True)
    picsrc = models.CharField(max_length= 10000)
    is_picked = models.BooleanField(default=False)

    def __str__(self):
        return self.name

def pre_save_collegedetails_receiver(sender,instance,*args,**kwargs):
    slug = slugify(instance.name)
    exists = CollegeDetails.objects.filter(slug=slug).exists()
    if exists:
        slug = "%s-%s" %(slug, instance.id)
    instance.slug = slug

pre_save.connect(pre_save_collegedetails_receiver, sender=CollegeDetails)

class Caste(models.Model):

    caste = models.CharField(max_length=20,blank=True)

    def __str__(self):
        return self.caste

class Location(models.Model):
    location = models.CharField(max_length=50,blank=True)
    def __str__(self):
        return self.location

class Field(models.Model):
    field_name = models.CharField(max_length = 100)
    def __str__(self):
        return self.field_name

class Map(models.Model):

        c = models.ForeignKey('CollegeDetails', on_delete = models.CASCADE)
        f = models.ForeignKey('Field', on_delete = models.CASCADE)
        caste = models.ForeignKey('Caste', on_delete = models.CASCADE)
        marks = models.IntegerField();
        location_map = models.CharField(max_length=200,blank=True)
        def __str__(self):
            return str(self.c)
