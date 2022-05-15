from django.db import models
from s3direct.fields import S3DirectField

def nameFile(instance, filename):
    return '/'.join(['images', str(instance.name), filename])

# Create your models here.
class Profile(models.Model):
    name=models.CharField(max_length=60)
    dob=models.DateField()
    email=models.EmailField()
    phone=models.CharField(max_length=15)
    address=models.CharField(max_length=100)
    image = models.ImageField(upload_to=nameFile, blank=True, null=True)
    subscription_start_date=models.DateField()
    subscription_end_date=models.DateField()
    password=models.CharField(max_length=50)
    def __str__(self):
        return self.name


class Courses(models.Model):
    CLASS_NUMBER = [
        ('1','One'),
        ('2', 'Two'),
        ('3', 'Three'),
        ('4', 'Four'),
        ('5', 'Five'),
        ('6', 'Six'),
        ('7', 'Seven'),
        ('8', 'Eight'),
        ('9', 'Nine'),
        ('10', 'Ten'),
        ('11', 'Eleven'),
        ('12', 'Twelve'),
    ]
    title=models.CharField(max_length=50)
    class_number=models.CharField(max_length=2,choices=CLASS_NUMBER , default='1')
    # class_number=models.CharField(max_length=2,choices=CLASS_NUMBER),
    video= models.FileField(upload_to='videos/', null=True, verbose_name="")

    def __str__(self):
        return self.title

class Batches(models.Model):
    batch_start=models.DateTimeField()
    batch_code=models.IntegerField()
    course=models.CharField(max_length=50)
    category=models.CharField(max_length=10, null=True, blank=True)
    subject=models.CharField(max_length=20, null=True, blank=True)
    timing=models.TimeField(null=True, blank=True)
    def __str__(self):
        return str(self.batch_code)

class Notification(models.Model):
    TYPES = [
            ('Announcement','Announcement'),
            ('Live Classes','Live Classes'),
            ('New Video','New Video'),

    ]
    title=models.CharField(max_length=50)
    notif_type=models.CharField(max_length=50,choices=TYPES , default='New Video')
    desc=models.CharField(max_length=500)
    def __str__(self):
        return self.title

class Admin(models.Model):
    username=models.CharField(max_length=50, unique=True)
    password=models.CharField(max_length=50)
    def __str__(self):
        return str(self.username)

class StudyMaterial(models.Model):
    CLASS_NUMBER = [
        ('1','One'),
        ('2', 'Two'),
        ('3', 'Three'),
        ('4', 'Four'),
        ('5', 'Five'),
        ('6', 'Six'),
        ('7', 'Seven'),
        ('8', 'Eight'),
        ('9', 'Nine'),
        ('10', 'Ten'),
        ('11', 'Eleven'),
        ('12', 'Twelve'),
    ]
    title=models.CharField(max_length=50)
    class_number=models.CharField(max_length=2,choices=CLASS_NUMBER , default='1')
    # class_number=models.CharField(max_length=2,choices=CLASS_NUMBER),
    material= models.FileField(upload_to='studymaterial/', null=True, verbose_name="")

    def __str__(self):
        return self.title
