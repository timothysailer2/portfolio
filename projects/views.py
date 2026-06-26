from multiprocessing import context

from django.shortcuts import render
from .import models

# Create your views here.
def projects(request):
    projectst = models.Project.objects.all().order_by('-year')
    context = { 'projects': projects }
    return render(request, 'projects/projects.html', context)