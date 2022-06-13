# views.py
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FileUploadParser, FormParser
from .serializers import UserSerializer, CourseSerializer, BatchSerializer, AdminSerializer, MaterialSerializer, NotifSerializer
from .models import Profile, Courses, Batches, Admin, StudyMaterial, Notification
from rest_framework.parsers import MultiPartParser,FormParser

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

    parser_classes = [MultiPartParser,FormParser]
    def create(self, request):
        video = request.FILES.getlist('video')

        for v in video:
            videoSerializer = CourseSerializer(data = {'title' : request.data.get('title'), 'class_number' : request.data.get('class_number'), 'video' : v})

            if videoSerializer.is_valid():
                videoSerializer.save()
            else:
                return Response(arr, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(status=status.HTTP_201_CREATED)


class MaterialViewSet(viewsets.ModelViewSet):
    queryset = StudyMaterial.objects.all().order_by('id')
    serializer_class = MaterialSerializer
    parser_classes = [MultiPartParser,FormParser]
    def create(self, request):
        material = request.FILES.getlist('material')

        for m in material:
            materialSerializer = MaterialSerializer(data = {'title' : request.data.get('title'), 'class_number' : request.data.get('class_number'), 'material' : m})

            if materialSerializer.is_valid():
                materialSerializer.save()
            else:
                return Response(arr, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(status=status.HTTP_201_CREATED)





class NotifViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all().order_by('id')
    serializer_class = NotifSerializer


class BatchViewSet(viewsets.ModelViewSet):
    queryset = Batches.objects.all().order_by('batch_code')
    serializer_class = BatchSerializer


class AdminViewSet(viewsets.ModelViewSet):
    queryset = Admin.objects.all().order_by('username')
    serializer_class = AdminSerializer
    lookup_field = 'username'


class APIRoot(APIView):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer

    def get(self, request):
        admin = AdminSerializer(Admin.objects.all(), many=True).data
        user = UserSerializer(Profile.objects.all(), many=True).data
        study_material = MaterialSerializer(
            StudyMaterial.objects.all(), many=True).data
        notification = NotifSerializer(
            Notification.objects.all(), many=True).data
        batch = BatchSerializer(Batches.objects.all(), many=True).data
        video = CourseSerializer(Courses.objects.all(), many=True).data
        # upload=ImageSerializer(Image.objects.all(),many=True).data
        return Response({
            "admins": admin,
            "user": user,
            "study_material": study_material,
            "notif": notification,
            "batch": batch,
            "video": video,


        })
