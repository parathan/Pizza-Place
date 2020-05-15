from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    context = {
        "regular": Regular.objects.all(),
        "toppings": Toppings.objects.all(),
    }
    return render(request, "PizzaTemplates/Index.html", context)

def register(request):
    return render(request, "PizzaTemplates/Register.html")

def loginview(request):
    return render(request, "PizzaTemplates/Login.html")

def registered(request):
    FirstName = request.POST["FirstName"]
    LastName = request.POST["LastName"]
    Email = request.POST["Email"]
    Username = request.POST["Username"]
    Password = request.POST["Password"]
    Passwordconfirm = request.POST["Password2"]
    if Password != Passwordconfirm:
        raise Http404("Passwords do not match")
    user = User.objects.create_user(Username, Email, Password)
    user.first_name = FirstName
    user.last_name = LastName
    user.save()
    return HttpResponseRedirect(reverse('index'))

def loginverify(request):
    Username = request.POST["username"]
    Password = request.POST["password"]
    user = authenticate(request, username=Username, password=Password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('index'))
    else:
        raise Http404("Invalid Credentials")
