from django.db import models

# Create your models here.
class Subject(models.Model):
	code = models.CharField(max_length=3, primary_key=True)
	name = models.CharField(max_length=64)

	def __str__(self):
		return f"{self.code} - {self.name}"


class Topic(models.Model):
	code = models.IntegerField()
	name = models.CharField(max_length=64)
	subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="topic")
	time = models.IntegerField(default=10)

	def __str__(self):
		return f"{self.subject.code}-{self.code} | {self.name}"



class Question(models.Model):
	topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="questions")
	question = models.CharField(max_length=1024)
	def __str__(self):
		return f"Q: {self.question}"

class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="choices")
	choice = models.CharField(max_length=100)
	value = models.BooleanField(default=False)
	def __str__(self):
		return f"Option - {self.choice}"

class Result(models.Model):
	user = models.CharField(max_length=64)
	topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="results")
	marks_obtained = models.IntegerField(default=0)
	marks_total = models.IntegerField(default=0)

	def __str__(self):
		return f"{self.user} scored {self.marks_obtained}/{self.marks_total} in {self.topic}"