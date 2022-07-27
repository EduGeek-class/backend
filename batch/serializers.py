# serializers.py
from rest_framework import serializers

from .models import Profile, Courses, Subjects,Batches, Admin, StudyMaterial, Notification


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        # course_codes = serializers.ListField(child=serializers.CharField())
        fields = ('id', 'name', 'dob', 'email', 'phone', 'address', 'image',
                  'subscription_start_date', 'subscription_end_date', 'password','batch_codes')

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = ('id', 'title', 'video','batch_code','subject_code')



class MaterialSerializer(serializers.ModelSerializer):
    material = serializers.FileField(max_length=None, allow_empty_file=False)
    class Meta:
        model = StudyMaterial
        fields = ('id', 'title', 'material','batch_code','subject_code')
        
class NotifSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ('id', 'title', 'notif_type', 'desc')

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subjects
        fields = ['subject_code', 'subject_name','batch_code']

class BatchSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Batches
        fields = ('batch_code','course_name','description','price','course_validity' ,'image',)


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ('username', 'password')


