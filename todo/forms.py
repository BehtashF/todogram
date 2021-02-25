from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    title = forms.CharField(label='', max_length=200, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'take a new task...','autocomplete':'off'}))
    description = forms.CharField(label='',widget=forms.Textarea(attrs={'class':'form-control mt-2', 'rows':3,'placeholder':'describe your task','autocomplete':'off'}))
    class Meta:
        model = Task
        fields = ['title', 'description',]