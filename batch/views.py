# views.py
from rest_framework import viewsets

from .serializers import UserSerializer,CourseSerializer,BatchSerializer
from .models import Profile,Courses,Batches


class UserViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all().order_by('name')
    serializer_class = UserSerializer
    def post(self, request, *args, **kwargs):
        file = request.data['file']
        image = UploadImageTest.objects.create(image=file)
        return HttpResponse(json.dumps({'message': "Uploaded"}), status=200)

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Courses.objects.all().order_by('title')
    serializer_class = CourseSerializer

class BatchViewSet(viewsets.ModelViewSet):
    queryset = Batches.objects.all().order_by('batch_code')
    serializer_class = BatchSerializer