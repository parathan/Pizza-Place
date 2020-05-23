from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Regular, Sicilian, Toppings, Subs, SubToppings, Pasta, Salads, Platters

# Create your views here.
