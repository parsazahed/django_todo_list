from django import forms
from todolist_app.models import Task

class Taskform(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task','done']