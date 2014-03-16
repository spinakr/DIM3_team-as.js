from django import forms
from django.contrib.auth.models import User 
from recap.models import UserProfile, RecapProject, Requirement, Category


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ()

class ProjectForm(forms.ModelForm):
    participants = forms.ModelMultipleChoiceField(queryset=User.objects.all())

    class Meta:
        model = RecapProject
        fields = ('name', 'description')

class RequirementForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'required':''}))
    # category = forms.ChoiceField(initial=Category.objects.get(index=0), choices=Category.objects.all().values_list('name', 'name'))
    
    #def clean(self):
    #    cleaned_data = self.cleaned_data
    #    category = cleaned_data.get('category')
    #    if category: 
    #        category = category.encode('utf-8')
    #        cleaned_data['category'] = category

    #    return cleaned_data
        
    
    class Meta:
        model = Requirement
        fields = ('name', 'description', 'category', 'responsible_person')
    
    


