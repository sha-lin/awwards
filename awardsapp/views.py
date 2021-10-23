from django.shortcuts import render, redirect
from django.contrib import messages
from django.http  import HttpResponse
from .models import Profile, Project, User
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, ProjectUploadForm, RateForm
from django.contrib.auth.decorators import login_required
from cloudinary.forms import cl_init_js_callbacks
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import Http404
from rest_framework import generics
from .serializers import ProfileSerializer, ProjectSerializer


# Create your views here.
def index(request):
    projects = Project.objects.all()
    users = User.objects.all()
    return render(request, 'index.html', {"projects":projects[::-1], "users": users})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Successfully created account created for {username}! Please log in to continue')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})

@login_required
def profile(request):
    projects = request.user.profile.projects.all()
    return render(request, 'users/profile.html', {"projects":projects[::-1]})

