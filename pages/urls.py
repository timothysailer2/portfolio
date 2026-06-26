from django.urls import path
from pages import views

urlpatterns = [
    path('', views.about_me_view, name='about_me'),

    path('about/', views.about_me_view, name='about_me'),

    path('contact/', views.contact_view, name='contact'),

    path('resume/', views.resume_view, name='resume'),
]