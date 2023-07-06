from django.shortcuts import render

# Create your views here.
from hr_athena.models import Question, Answer
import random


def home(request):
    random_questions = []
    questions = Question.objects.all()
    set_of_id = {1}
    for question in range(5):
        id = random.randint(0, 10)
        set_of_id.add(id)
    for id in set_of_id:
        random_questions.append(questions[id])
    answers = Answer.objects.all()
    return render(request, 'hr_athena/home.html', {"questions": random_questions, "answers": answers})
