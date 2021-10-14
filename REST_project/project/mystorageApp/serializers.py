from rest_framework import serializers
from .models import Album, Essay, File

class EssaySerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Essay
        fields = ['pk', 'title', 'body', 'author',]

class AlbumSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    image = serializers.ImageField(use_url=True)
    class Meta:
        model = Album
        fields = ['pk', 'image', 'desc', 'author',]


class FileSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    file = serializers.FileField(use_url=True)
    class Meta:
        model = File
        fields = ['pk', 'file', 'desc', 'author',]