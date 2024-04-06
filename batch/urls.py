# myapi/urls.py
from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
from batch import views
import re
# router = routers.DefaultRouter()
# # router.register(r'',views.APIRoot.as_view(),'root')
# router.register(r'profiles', views.UserViewSet)
# router.register(r'courses',views.CourseViewSet)
# router.register(r'material',views.MaterialViewSet)
# router.register(r'batches',views.BatchViewSet)
# router.register(r'site-admin',views.AdminViewSet)
# router.register(r'notif',views.NotifViewSet)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
# urlpatterns = router.urls
urlpatterns=[
    path('',views.APIRoot.as_view()),
    path('user/',views.UserViewSet.as_view({
        'get':'list',
        'post':'create',
        

    })),
    path('user/<int:pk>',views.UserViewSet.as_view({
        'get':'retrieve',
        
        'patch':'partial_update',
        'delete':'destroy'
        

    })), path('study_material/',views.MaterialViewSet.as_view({
        'get':'list',
        'post':'create',
        

    })),
    path('study_material/<int:pk>',views.MaterialViewSet.as_view({
        'get':'retrieve',
        
        'patch':'partial_update',
        'delete':'destroy'
        

    })), 
        path('study_material/batch_code/<int:batch_code>', views.MaterialByBatchCodeAPIView.as_view(), name='material-by-batch'),

    path('video/',views.CourseViewSet.as_view({
        'get':'list',
        'post':'create',
        

    })),
    path('video/<int:pk>',views.CourseViewSet.as_view({
        'get':'retrieve',
        
        'patch':'partial_update',
        'delete':'destroy'
        

    })), path('notif/',views.NotifViewSet.as_view({
        'get':'list',
        'post':'create',
        

    })),
    path('notif/<int:pk>',views.NotifViewSet.as_view({
        'get':'retrieve',
        
        'patch':'partial_update',
        'delete':'destroy'
        

    })), path('subject/',views.SubjectViewSet.as_view({
        'get':'list',
        'post':'create',
        

    })),
    path('subject/<int:pk>',views.SubjectViewSet.as_view({
        'get':'retrieve',
        
        'patch':'partial_update',
        'delete':'destroy'
        

    }))
    , path('batch/',views.BatchViewSet.as_view({
        'get':'list',
        'post':'create',
        

    })),
    path('batch/<int:pk>',views.BatchViewSet.as_view({
        'get':'retrieve',
        
        'patch':'partial_update',
        'delete':'destroy'
        

    })),
     path('admins/',views.AdminViewSet.as_view({
        'get':'list',
        'post':'create',
        

    })),
   
        
     
    
   
    
]
    # path('upload/', views.UserViewSet.as_view(), name='upload')


# urls for get and post has been updated
