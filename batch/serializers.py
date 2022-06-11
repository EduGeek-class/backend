# serializers.py
from rest_framework import serializers

from .models import Profile,Courses,Batches, Admin,StudyMaterial,Notification

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('id','name', 'dob','email','phone','address','image','subscription_start_date','subscription_end_date', 'password')


# class ImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UploadImageTest
#         fields = ('name', 'image')

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = ('id','title','class_number','video')

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyMaterial
        fields = ('id','title','class_number','material')

class NotifSerializer(serializers.ModelSerializer):
     class Meta:
        model = Notification
        fields = ('id','title','notif_type','desc')

class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batches
        fields = ('id','batch_start','batch_code','course','category','subject','timing')

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ('username', 'password')

        

 