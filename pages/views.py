from django.shortcuts import render

# Create your views here.
def about_me_view(request):
    return render(request, 'pages/about_me.html')

def projects_view(request):
    return render(request, 'pages/projects.html')

def contact_view(request):
    return render(request, 'pages/contact.html')

def resume_view(request):
    return render(request, 'pages/resume.html')
