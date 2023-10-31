from django import forms
from .models import JobApplication, JobList, UserProfile

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['name', 'phone', 'email', 'location', 'resume', 'latest_qualification']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'resume': forms.FileInput(attrs={'class': 'form-control-file'}),
            'latest_qualification': forms.TextInput(attrs={'class': 'form-control'}),
        }

class JobListForm(forms.ModelForm):
    class Meta:
        model = JobList
        fields = ['title', 'description', 'location', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'linkedin_profile', 'website']
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            'linkedin_profile': forms.TextInput(attrs={'class': 'form-control'}),
            'website': forms.TextInput(attrs={'class': 'form-control'}),
        }


