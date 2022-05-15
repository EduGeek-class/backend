# views.py
from rest_framework import viewsets

from .serializers import UserSerializer, CourseSerializer, BatchSerializer, AdminSerializer ,MaterialSerializer
from .models import Profile, Courses, Batches, Admin,StudyMaterial


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

class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Courses.objects.all().order_by('id')
    serializer_class = MaterialSerializer

class BatchViewSet(viewsets.ModelViewSet):
    queryset = Batches.objects.all().order_by('batch_code')
    serializer_class = BatchSerializer
class AdminViewSet(viewsets.ModelViewSet):
    queryset = Admin.objects.all().order_by('username')
    serializer_class = AdminSerializer
    lookup_field = 'username'