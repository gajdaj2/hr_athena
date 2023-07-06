import PyPDF2
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate

# Create your views here.
from hr_athena.models import Question, Answer
from manager.forms import QuestionForm, QuestionTable, AnswerTable, CVForm, JobPositionTable, SkillsTable, \
    JobPositionForm, SkillsForm
from manager.models import JobPosition, Skills
from manager.analysis.text_summerization import cv_summarize, cv_question


def pos_details(request, pk):
    position = get_object_or_404(JobPosition, pk=pk)
    if request.method == "GET":
        position = get_object_or_404(JobPosition, pk=pk)
        skills = Skills.objects.filter(job_position=position)
        form = SkillsForm()
        table = SkillsTable(skills, template_name='django_tables2/bootstrap5.html')
        return render(request, 'manager/pos_details.html', {"skills": table, "form": form})
    else:
        form = SkillsForm(request.POST)
        if form.is_valid():
            skill = Skills(skill=request.POST['skill'], skill_type=request.POST['skill_type'], job_position=position)
            skill.save()
            return redirect('manager:positions')


def positions(request):
    if request.method == "GET":
        jobPositions = JobPosition.objects.all()
        position_form = JobPositionForm()
        table = JobPositionTable(jobPositions, template_name='django_tables2/bootstrap5.html')
        return render(request, 'manager/positions.html', {"positions": table, "form": position_form})
    else:
        form = JobPositionForm(request.POST)
        if form.is_valid():
            job_position = JobPosition(title=request.POST['title'], level=request.POST['level'])
            job_position.save()
            return redirect('manager:positions')


def gen_profile(request):
    if request.method == "GET":
        return render(request, 'manager/genprofile.html')


def loginuser(request):
    if request.method == "GET":
        return render(request, 'manager/login.html')
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'manager/login.html', {"error": "You provide wrong password or email"})
        else:
            login(request, user)
            return redirect('manager:home')


def logoutuser(request):
    if request.method == "POST":
        logout(request)
        return redirect('manager:loginuser')
    else:
        return redirect('manager:loginuser')


def home(request):
    if request.method == "GET":
        questions = Question.objects.all()
        table = QuestionTable(questions, template_name='django_tables2/bootstrap5.html')
        table.paginate(page=request.GET.get("page", 1), per_page=10)
        return render(request, 'manager/home.html', {"table": table})
    else:
        finding = Question.objects.filter(question__contains=request.POST['search']).all()
        table = QuestionTable(finding, template_name='django_tables2/bootstrap5.html')
        table.paginate(page=request.GET.get("page", 1), per_page=10)
        return render(request, 'manager/home.html', {"table": table})


def details(request, pk):
    if request.method == 'GET':
        question = get_object_or_404(Question, pk=pk)
        answers = Answer.objects.filter(question=question)
        table = AnswerTable(answers, template_name='django_tables2/bootstrap5.html')
        return render(request, 'manager/details.html', {"question": question, "answers": table})
    else:
        question = get_object_or_404(Question, pk=pk)
        answer = Answer(question=question, answer=request.POST['answer'], is_true=is_true_answer(request))
        answers = Answer.objects.filter(question=question)
        table = AnswerTable(answers, template_name='django_tables2/bootstrap5.html')
        answer.save()
        return render(request, 'manager/details.html', {"question": question, "answers": table})


def is_true_answer(request):
    is_True = False
    if 'is_true' in request.POST:
        is_True = True
    else:
        is_True = False
    return is_True


def answer(request, pk):
    if request.method == 'GET':
        answer = get_object_or_404(Answer, pk=pk)
        return render(request, 'manager/answer.html', {'answer': answer})
    else:
        new_record = Answer.objects.filter(pk=pk).get()
        if 'new_is_true' in request.POST:
            new_record.answer = request.POST['new_answer']
            new_record.is_true = True
            new_record.save()
        else:
            new_record.answer = request.POST['new_answer']
            new_record.is_true = False
            new_record.save()
        return redirect('manager:home')


def add_question(request):
    if request.method == 'GET':
        form_question = QuestionForm()
        return render(request, 'manager/add_question.html', {"form_question": form_question})
    else:
        question = request.POST['question']
        language = request.POST['language']
        type = request.POST['type']

        question = Question(question=question, language=language, type=type)
        question.save()
        return redirect('manager:home')


def cvanalysis(request):
    cvform = CVForm(request.POST, request.FILES)
    if request.method == 'GET':
        jobPositions = JobPosition.objects.all()
        return render(request, 'manager/cvanalysis.html', {"cvform": cvform, "postions": jobPositions})
    else:
        jobPositions = JobPosition.objects.all()
        max_score = Skills.objects.filter(job_position=int(request.POST['options'])).count()
        file = ""
        pdfReader = PyPDF2.PdfReader(request.FILES['filepath'])
        for x in range(len(pdfReader.pages)):
            filePage = pdfReader.pages[x]
            file += filePage.extract_text(0)
        # candidate_skill = file.split(" ",",")
        # lower_candidate_skill = [skill.lower() for skill in candidate_skill]
        skills_to_check = Skills.objects.filter(job_position=int(request.POST['options']))
        candiate_skill_checked = []

        for skill in skills_to_check:
            if skill.skill.lower() in file.lower():
                candiate_skill_checked.append(skill)

        cv_sum = cv_summarize(file)
        question = request.POST['question']
        answer = cv_question(question=question, text=file)

        return render(request, 'manager/cvanalysis.html',
                      {"cvform": cvform, "file": file, "max_score": max_score,
                       "canidate_score": len(candiate_skill_checked),
                       "postions": jobPositions, 'skills': candiate_skill_checked,
                       "cv_summarize": cv_sum, "answer": answer})
