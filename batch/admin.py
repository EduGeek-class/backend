from django.contrib import admin
from .models import Profile, Courses, Batches, Admin
admin.register(Profile, Courses, Batches, Admin)(admin.ModelAdmin)