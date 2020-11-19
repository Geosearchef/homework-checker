from apps.homework.models import Exercise
from rest_framework import permissions, response, status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from sendfile import sendfile

from ..models import Lecture, LectureResource, Lesson, LessonResource
from .serializers import LessonDetailSerializer


class LectureSignUp(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        lecture = Lecture.objects.get(slug=kwargs["lecture_slug"])
        lecture.participants.add(request.user)
        lecture.save()
        return response.Response({}, status=status.HTTP_200_OK)


class LectureStatus(APIView):
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "lecture_slug"

    def get(self, request, *args, **kwargs):
        lecture = Lecture.objects.get(slug=kwargs["lecture_slug"])
        data = {"registered": request.user in lecture.participants.all()}
        return response.Response(data, status=status.HTTP_200_OK)


class LessonRetrieveView(RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = LessonDetailSerializer

    def get_object(self):
        lecture_slug = self.kwargs["lecture_slug"]
        lesson_slug = self.kwargs["lesson_slug"]
        return Lesson.objects.get(lecture__slug=lecture_slug, slug=lesson_slug)


class LectureResourceDownload(RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        lecture_slug = self.kwargs["lecture_slug"]
        resource_id = self.kwargs["resource_id"]
        resource = LectureResource.objects.get(lecture__slug=lecture_slug, id=resource_id)
        if resource.public:
            return sendfile(request, resource.file.path, attachment=True)


class LessonResourceDownload(RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        lecture_slug = self.kwargs["lecture_slug"]
        lesson_slug = self.kwargs["lesson_slug"]
        resource_id = self.kwargs["resource_id"]
        resource = LessonResource.objects.get(
            lesson__lecture__slug=lecture_slug,
            lesson__slug=lesson_slug,
            id=resource_id,
        )
        if resource.public:
            return sendfile(request, resource.file.path, attachment=True)
