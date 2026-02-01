from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import generics, views
from rest_framework.response import Response
from rest_framework import authentication, permissions

from . import serializers
from . import models

class UsersAPIView(generics.ListAPIView):
    serializer_class = serializers.UserModelSerializer

    def get_queryset(self):
        return models.UserModel.objects.all().order_by('id')



class CategoryAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.CategoryModelSerializer
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
    
        return models.ProductCategory.objects.prefetch_related(
            'products'   
        )

    def perform_create(self, serializer):
        serializer.save()


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.CategoryModelSerializer
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return models.ProductCategory.objects.prefetch_related(
            'products'
        )
        
