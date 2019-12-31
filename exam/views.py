from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.urls import reverse

# Create your views here.

def index(request):
	if not request.user.is_authenticated:
		return render(request, "exam/login.html", {"message": None})

	return render(request, "exam/index.html")

def login_view(request):
	username = request.POST["username"]
	password = request.POST["password"]
	user = authenticate(request, username=username, password=password)
	if user is not None:
		login(request, user)
		return HttpResponseRedirect(reverse("index"))
	else:
		return render(request, "exam/login.html", {"message": "Invalid Credentials"})

def logout_view(request):
	logout(request)
	return render(request, "exam/login.html", {"message": "Logged Out"})


def register_view(request):
	username = request.POST["username"]
	password = request.POST["password"]
	email = request.POST["email"]

	user = User.objects.create_user(username, email, password)
	user.first_name = request.POST["first"]
	user.last_name = request.POST["last"]
	user.save()
	login(request, user)

	return HttpResponseRedirect(reverse("index"))
