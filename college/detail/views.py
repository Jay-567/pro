from django.shortcuts import render
from django.http import HttpResponse
from detail.models import CollegeModel
from detail.serializer import CollegeSerializer
from rest_framework import viewsets


class CollegeViews(viewsets.ModelViewSet):
    querset =  CollegeModel.objects.all()
    serializer_class = CollegeSerializer


# Create your views here.
