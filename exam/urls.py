from django.urls import path

from . import views

urlpatterns = [
	path("", views.index, name="index"),
	path("login", views.login_view, name="login"),
	path("search", views.search_view, name="search"),
	path("logout", views.logout_view, name="logout"),
	path("register", views.register_view, name="register"),
	path("<str:subject_code>", views.topic_view, name="topics"),
	path("instructions/<int:topic_id>", views.instruction_view, name="instructions"),
	path("test/<int:topic_id>", views.test_view, name="test"),
	path("test/score/<int:topic_id>", views.score_calculator, name="score"),
	
]