from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from .models import Profile
from django.http import HttpResponse
from django.template import loader
import pdfkit
import io

# Create your views here.
@login_required
def profile(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        school = request.POST['school']
        degree = request.POST['degree']
        university = request.POST['university']
        skill = request.POST['skill']
        about_you = request.POST['about_you']
        previous_projects = request.POST['previous_projects']
        user_id = request.user.id

        profile = Profile(name=name, email=email, phone=phone, school=school, degree=degree,
                          university=university, skill=skill, about_you=about_you, previous_projects=previous_projects,
                          user_id=user_id)
        profile.save()
        return redirect('/')
    else:
        return render(request, 'index.html')
@login_required
def resume(request):
    user = request.user
    print(user)
    user_profile = Profile.objects.filter(user=user).last
    template = loader.get_template("resume.html")
    html = template.render({'user':user_profile})
    option = {'page-size':'letter','encoding':'UTF-8'}
    pdf = pdfkit.from_string(html, False,option)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['content-Disposition']= 'attachments'
    return response

