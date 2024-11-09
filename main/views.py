# Create your views here.

from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (
    ListModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
)

from main.models import Student
from main.serializers import StudentSerializer


class StudentListAPIView(ListModelMixin, CreateModelMixin, GenericAPIView):
    """
    GET: 학생 목록 조회
    POST: 학생 추가
    """

    ### assignment2: 이곳에 과제를 작성해주세요
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    ### end assignment2


class StudentAPIView(
    RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericAPIView
):
    """
    GET: 학생 조회
    PATCH: 학생 수정
    DELETE: 학생 삭제
    """

    ### assignment2: 이곳에 과제를 작성해주세요
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    ### end assignment2
