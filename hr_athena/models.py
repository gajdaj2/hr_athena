from django.db import models

# Create your models here.
from django.forms import forms
from django.views.generic import CreateView


class Question(models.Model):
    question = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    type = models.CharField(max_length=255)

    def __str__(self):
        return self.question


class Answer(models.Model):
    answer = models.CharField(max_length=255)
    is_true = models.BooleanField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.answer



