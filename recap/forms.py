from django import forms
from django.contrib.auth.models import User
from recap.models import UserProfile, RecapProject


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('role',)


class ProjectForm(forms.ModelForm):
    participants = forms.ModelMultipleChoiceField(queryset=User.objects.all())

    class Meta:
        model = RecapProject
        fields = ('name', 'description')
