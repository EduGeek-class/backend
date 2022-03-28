# serializers.py
from rest_framework import serializers

from .models import Profile,Courses,Batches

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('name', 'dob','email','phone','address','image')

# class ImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UploadImageTest
#         fields = ('name', 'image')

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = ('title','class_number','video')

class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batches
        fields = ('batch_start','batch_code','course','category','subject','timing')

 