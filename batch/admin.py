from django.contrib import admin
from .models import Profile, Courses, Batches, Admin,StudyMaterial,Notification
admin.register(Profile, Courses,StudyMaterial, Batches, Admin ,Notification)(admin.ModelAdmin)