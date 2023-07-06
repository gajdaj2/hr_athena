from django.contrib import admin

# Register your models here.
from manager.models import JobPosition, Skills

admin.site.register(JobPosition)
admin.site.register(Skills)
