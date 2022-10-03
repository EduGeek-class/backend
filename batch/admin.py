from django.contrib import admin
from .models import Profile, Courses,Subjects, Batches, Admin,StudyMaterial,Notification
admin.register(Profile, Courses,StudyMaterial, Subjects,Batches, Admin ,Notification)(admin.ModelAdmin)

# To make changes in the django admin