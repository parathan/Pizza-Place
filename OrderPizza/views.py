from django.shortcuts import render
from rest_framework import viewsets

from .serializers import RegularSerializer, SicilianSerializer, ToppingsSerializer, SubsSerializer, SubToppingsSerializer, PastaSerializer, SaladsSerializer, PlattersSerializer
from .models import Regular, Sicilian, Toppings, Subs, SubToppings, Pasta, Salads, Platters

# Create your views here.
class RegularViewSet(viewsets.ModelViewSet):
    queryset = Regular.objects.all()
    serializer_class = RegularSerializer

class SicilianViewSet(viewsets.ModelViewSet):
    queryset = Sicilian.objects.all()
    serializer_class = SicilianSerializer

class ToppingsViewSet(viewsets.ModelViewSet):
    queryset = Toppings.objects.all()
    serializer_class = ToppingsSerializer

class SubsViewSet(viewsets.ModelViewSet):
    queryset = Subs.objects.all()
    serializer_class = SubsSerializer

class SubToppingsViewSet(viewsets.ModelViewSet):
    queryset = SubToppings.objects.all()
    serializer_class = SubToppingsSerializer

class PastaViewSet(viewsets.ModelViewSet):
    queryset = Pasta.objects.all()
    serializer_class = PastaSerializer

class SaladsViewSet(viewsets.ModelViewSet):
    queryset = Salads.objects.all()
    serializer_class = SaladsSerializer

class PlattersViewSet(viewsets.ModelViewSet):
    queryset = Platters.objects.all()
    serializer_class = PlattersSerializer
