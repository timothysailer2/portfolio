from multiprocessing import context
from django.http import HttpResponse
from django.core.mail import send_mail

from django.shortcuts import render
from .import models

# Create your views here.
def projects(request):
    projects = models.Project.objects.all().order_by('-year')
    context = { 'projects': projects }
    return render(request, 'projects/projects.html', context)

