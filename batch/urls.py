# myapi/urls.py
from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
from batch import views
import re
router = routers.DefaultRouter()
router.register(r'profiles', views.UserViewSet)
router.register(r'courses',views.CourseViewSet)
router.register(r'batches',views.BatchViewSet)
router.register(r'site-admin',views.AdminViewSet)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = router.urls
    # path('upload/', views.UserViewSet.as_view(), name='upload')


