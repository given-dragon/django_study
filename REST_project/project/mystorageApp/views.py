from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import parsers
from . import models, serializers
from rest_framework.filters import SearchFilter
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = models.Essay.objects.all()
    serializer_class = serializers.EssaySerializer

    #search기능 추가
    filter_backends = [SearchFilter]
    search_fields = ('title', 'body', )


    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        #현재 유저는 self.request.user
        qs = super().get_queryset()

        if self.request.user.is_authenticated:
            if self.request.user.is_superuser:
                pass    #superuser는 모든 글 조회 가능
            else:
                #본인의 글만 filtering해서 queryset에 담는다
                qs = qs.filter(author=self.request.user)
        else:
            qs = qs.none()
        return qs

class ImageViewSet(viewsets.ModelViewSet):
    queryset = models.Album.objects.all()
    serializer_class = serializers.AlbumSerializer

class FileViewSet(viewsets.ModelViewSet):
    queryset = models.File.objects.all()
    serializer_class = serializers.FileSerializer
    parser_classes = (MultiPartParser, FormParser,) #다양한 미디어 type에 대한 수락 방식을 등록해줌

    def post(self, request, *args, **kwargs):
        serializer = serializers.FileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
