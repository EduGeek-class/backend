# serializers.py
from rest_framework import serializers

from .models import Profile, Courses, Batches, Admin, StudyMaterial, Notification


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        # course_codes = serializers.ListField(child=serializers.CharField())
        fields = ('id', 'name', 'dob', 'email', 'phone', 'address', 'image',
                  'subscription_start_date', 'subscription_end_date', 'password','batch_codes')

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = ('id', 'title', 'video','batch_code')



class MaterialSerializer(serializers.ModelSerializer):
    material = serializers.FileField(max_length=None, allow_empty_file=False)
    class Meta:
        model = StudyMaterial
        fields = ('id', 'title', 'material','batch_code')
        
class NotifSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ('id', 'title', 'notif_type', 'desc')


class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batches
        fields = ('batch_start', 'batch_code',
                  'course', 'category', 'subject' )


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ('username', 'password')


