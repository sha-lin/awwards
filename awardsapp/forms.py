from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Project, Rating, RATE_CHOICES

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_photo', 'bio']

class ProjectUploadForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'project_image', 'description', 'link' ]

    def form_valid(self, form):
        form.instance.user = self.request.profile
        return super().form_valid(form)

class RateForm(forms.ModelForm):
    rate_design = forms.ChoiceField(choices=RATE_CHOICES, widget = forms.Select(), required = True)
    rate_usability = forms.ChoiceField(choices=RATE_CHOICES, widget = forms.Select(), required = True)
    rate_content = forms.ChoiceField(choices=RATE_CHOICES, widget = forms.Select(), required = True)

    class Meta:
        model = Rating
        fields = ['rate_design', 'rate_usability', 'rate_content' ]
