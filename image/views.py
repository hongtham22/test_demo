from django.shortcuts import render

# Create your views here.
#demo/image/views.py
from image.models import Image
from image.serializers import ImageSerializer
from rest_framework import viewsets


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

