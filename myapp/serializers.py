from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from PIL import Image
from rest_framework import serializers

class ImageSerializer(serializers.Serializer):
    image = serializers.ImageField()
