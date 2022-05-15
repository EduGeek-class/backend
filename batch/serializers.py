# serializers.py
from rest_framework import serializers

from .models import Profile,Courses,Batches, Admin

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('name', 'dob','email','phone','address','image','subscription_start_date','subscription_end_date')


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

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ('username', 'password')

 