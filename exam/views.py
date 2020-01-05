from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.urls import reverse

# Create your views here.
from .models import Subject, Topic, Question, Choice, Result

def index(request):
	if not request.user.is_authenticated:
		return render(request, "exam/login.html", {"message": None})
	fname = request.user.first_name
	activity = Result.objects.filter(user=fname)


	context = {
		"subjects" : Subject.objects.all(),
		"activities": activity,
		"user": fname,
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
	fname = request.user.first_name
	activity = Result.objects.filter(user=fname)
	context = {
		"topics": topics,
		"activities": activity,
		"user": fname,
	}

	return render(request, "exam/topics.html", context)


def test_view(request, topic_id):
	print("im in test")
	questions = Question.objects.filter(topic=topic_id)
	fname = request.user.first_name
	activity = Result.objects.filter(user=fname)
	context = {
		"questions": questions,
		"topicid": topic_id,
		"activities": activity,
		"user": fname,
	}

	return render(request, "exam/test.html", context)	


def score_calculator(request, topic_id):
	if request.method == "POST":
		fname = request.user.first_name
		topic = Topic.objects.get(pk=topic_id)
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
		total_marks = len(actual_answer)			
		for i in range(len(response)):
			if response[i] == actual_answer[i]:
				marks += 1
		print(f"Marks are {marks} out of {total_marks}")


		result = Result(user=fname, topic=topic, marks_obtained=marks, marks_total=total_marks)
		result.save()

		fname = request.user.first_name
		activity = Result.objects.filter(user=fname)

		context = {
			"marks": marks,
			"topic": topic,
			"marks_total": total_marks,
			"user": fname,
			"actual_answer": actual_answer,
			"response": response,
			"var": zip(actual_answer, response),
			"activities": activity,
			"user": fname,


		}


		return render(request, "exam/result.html", context)
