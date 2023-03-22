
from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('resume/', views.resume, name='resume'),
    # other URL patterns for the blog app...
]


