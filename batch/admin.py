from django.contrib import admin
from .models import Profile, Courses, Batches, Admin,StudyMaterial
admin.register(Profile, Courses,StudyMaterial, Batches, Admin)(admin.ModelAdmin)