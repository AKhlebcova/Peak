from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import permissions

from pereval.serializers import *
from pereval.models import *






class UsersViewset(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    # def create(self, request, *args, **kwargs):
    #     print('1111!!')
    #     return super().create(request, *args, **kwargs)


class CoordsViewset(viewsets.ModelViewSet):
    queryset = Coords.objects.all()
    serializer_class = CoordsSerializer


class AddViewset(viewsets.ModelViewSet):
    queryset = Add.objects.all()
    serializer_class = AddSerializer

class ImagesViewset(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer


from django.shortcuts import render

# Create your views here.
