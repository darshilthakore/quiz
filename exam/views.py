from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.urls import reverse

# Create your views here.
from .models import Subject, Topic, Question, Choice

def index(request):
	if not request.user.is_authenticated:
		return render(request, "exam/login.html", {"message": None})


	context = {
		"subjects" : Subject.objects.all(),
	}

	return render(request, "exam/index.html", context)

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


def topic_view(request, subject_code):
	print("im in topic_view")
	topics = Topic.objects.filter(subject=subject_code)
	context = {
		"topics": topics,
	}

	return render(request, "exam/topics.html", context)


def test_view(request, topic_id):
	print("im in test")
	questions = Question.objects.filter(topic=topic_id)
	context = {
		"questions": questions,
		"topicid": topic_id,
	}

	return render(request, "exam/test.html", context)	


def score_calculator(request, topic_id):
	if request.method == "POST":
		print("im in score_calculator")
		marks = 0
		print(f"marks are {marks}")
		questions = Question.objects.filter(topic=topic_id)
		response = []
		for question in questions:
			print(f"id is {question.id}")
			r = question.id
			m = request.POST.get(str(r),'')

			print(f"response for {question} is : {m}")
			response.append(m)
			# if resp == question.choices.value:
			# 	marks += 1
		print(f"answers by user is: {response}")
		actual_answer = []
		for question in questions:
			choices = question.choices.filter(question=question)
			for choice in choices:
				if choice.value == True:
					actual_answer.append(choice.choice)
		print(f"actual answers : {actual_answer}")			
		for i in range(len(response)):
			if response[i] == actual_answer[i]:
				marks += 1
		print(f"Marks are {marks} out of {len(actual_answer)}")


		return render(request, "exam/index.html")
