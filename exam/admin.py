from django.contrib import admin

# Register your models here.
from .models import Subject, Topic, Question, Choice, Result


class ChoiceInlines(admin.TabularInline):
	model = Choice

class QuestionAdmin(admin.ModelAdmin):
	inlines = [ChoiceInlines]

admin.site.register(Subject)
admin.site.register(Topic)
admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)
admin.site.register(Result)