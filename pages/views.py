from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse

# Create your views here.
def about_me_view(request):
    return render(request, 'pages/about_me.html')

def projects_view(request):
    return render(request, 'pages/projects.html')

def resume_view(request):
    return render(request, 'pages/resume.html')

def contact_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        full_message = f"From: {name}\nEmail: {email}\n\nMessage:\n{message}"

        send_mail(
            subject="New Contact Form Submission",
            message=full_message,
            from_email="tim.sailer283@gmail.com",   # must match EMAIL_HOST_USER
            recipient_list=["tim.sailer283@gmail.com"],
        )

        return HttpResponse("Message sent!")

    return render(request, "pages/contact.html")



