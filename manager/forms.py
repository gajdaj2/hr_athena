from django import forms
import django_tables2 as tables
from django_tables2 import A

from hr_athena.models import Question, Answer
from manager.models import JobPosition, Skills, SKILL_TYPE

LANGUAGES = (('', 'Choose ...'), ('Java', 'Java'), ('Python', 'Python'), ('Javascript', 'Javascript'))
TYPE = (('OPEN', 'OPEN'), ('CLOSED', 'CLOSED'))
JOB_POSITION = (('Java Test Automation, Senior'), ('Java Test Automation Junior'))


class QuestionForm(forms.Form):
    question = forms.CharField(max_length=255)
    language = forms.ChoiceField(choices=LANGUAGES)
    type = forms.ChoiceField(choices=TYPE)


class TranscriptForm(forms.Form):
    question = forms.CharField(max_length=255)
    filepath = forms.FileField()


class CVForm(forms.Form):
    job_position_form = forms.ChoiceField(choices=JOB_POSITION)
    filepath = forms.FileField()


class QuestionTable(tables.Table):
    detail = tables.LinkColumn('manager:details', text='details', args=[A('pk')])

    class Meta:
        model = Question


class AnswerTable(tables.Table):
    change = tables.LinkColumn('manager:answer', text='change', args=[A('pk')])

    class Meta:
        model = Answer


class JobPositionTable(tables.Table):
    detail = tables.LinkColumn('manager:pos_details', text='details', args=[A('pk')])

    class Meta:
        model = JobPosition


class SkillsTable(tables.Table):
    class Meta:
        model = Skills


class JobPositionForm(forms.Form):
    title = forms.CharField(max_length=255)
    level = forms.CharField(max_length=255)


class SkillsForm(forms.Form):
    skill = forms.CharField(max_length=255)
    skill_type = forms.ChoiceField(choices=SKILL_TYPE)
