from django.db import models

# Create your models here.

SKILL_TYPE = (
    ('TECHNICAL', 'TECHNICAL'),
    ('PROCESS', 'PROCESS'),
    ('LANGUAGE', 'LANGUAGE'),
    ('PERSONAL', 'PERSONAL'),
)


class JobPosition(models.Model):
    title = models.CharField(max_length=255)
    level = models.CharField(max_length=255)

    def __str__(self):
        return self.title + ", " + self.level


class Skills(models.Model):
    skill = models.CharField(max_length=255)
    skill_type = models.CharField(max_length=255, choices=SKILL_TYPE, default='TECHNICAL')
    job_position = models.ForeignKey(JobPosition, on_delete=models.CASCADE)

    def __str__(self):
        return self.skill


class Candidate(models.Model):
    linkedin = models.CharField(max_length=255)
    cv = models.CharField(max_length=255)
    job_position = models.ForeignKey(JobPosition, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + ", " + self.job_position.title


class Analysis(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    summary = models.CharField(max_length=2000)
    facts = models.CharField(max_length=2000)
    analysis_questions = models.CharField(max_length=2000)
    analysis_answer = models.CharField(max_length=2000)
    interview_questions = models.CharField(max_length=5000)

    def __str__(self):
        return self.candidate.name + ", " + \
            self.candidate.job_position.title
