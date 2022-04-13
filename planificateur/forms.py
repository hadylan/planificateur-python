from pkg_resources import require
from planificateur.models import Developer, Report, Task, Project, StatusChoice
from django.forms import ModelForm, Textarea
from django import forms

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["desc", "duree", "priority", "startingDate", "developers"]
        
        
class ProjectForm(ModelForm):
    #developers = forms.ModelMultipleChoiceField(queryset=Developer.objects.all())
    class Meta:
        model = Project
        fields = ["status", "desc", "startingDate", "deliveryDate", "stateOfProgress", "name", "id_projectManager"]
    

class ReportForm(ModelForm):
    class Meta:
        model = Report
        fields = ["content"]

class StatusForm(ModelForm):
    model = StatusChoice

class CreateDevForm(ModelForm):
    class Meta:
        model = Developer
        fields = ["firstname", "lastname"]