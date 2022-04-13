from re import T
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse

from planificateur.forms import ReportForm, StatusForm, TaskForm, ProjectForm, CreateDevForm
from .models import AssReport_Task, Report, Task, StatusChoice, Developer, AssDev_Task, Project, AssProject_Task
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.conf import settings

# Create your views here.
def index(request):
    context = {'userConnected': userConnected()}
    return render(request, 'planificateur/hello.html', context)

def getOneTask(request, task_id, project_id):
    task = Task.objects.get(pk=task_id)
    developer_list = Developer.objects.all().exclude(id__in=task.developers.all())
    context = {
        "task": task,
        "developer_list": developer_list,
        "project_id": project_id,
    }
    return render(request, 'planificateur/task.html', context)

def addTask(request, project_id):
    if(request.method == "POST"):
        formTask=TaskForm(request.POST)
        if formTask.is_valid():
            formTask.save()
            assProjectTask = AssProject_Task()
            assProjectTask.id_project = Project.objects.get(pk=project_id)
            assProjectTask.id_task = formTask.instance
            assProjectTask.save()
            return redirect('getOneProject', id=project_id)
    else:
        formTask = TaskForm()
        context = {
            'formTask': formTask,
            'isEdit': False,
            "project_id": project_id
        }
        return render(request, 'planificateur/form_task.html', context)

def updateTask(request, task_id, project_id):
    if(request.method == "POST"):
        formTask=TaskForm(request.POST)
        if formTask.is_valid():
            taskToUpdate = Task.objects.get(pk=task_id)
            taskToUpdate = formTask
            taskToUpdate.save()
            return redirect('getOneTask', task_id=formTask.instance.id, project_id=project_id)
    else:
        task = Task.objects.get(pk=task_id)
        formTask = TaskForm(instance=task)
        context = {
            'formTask': formTask,
            'task_id': task_id,
            'isEdit': True,
            'project_id': project_id
        }
        return render(request, 'planificateur/form_task.html', context)

def deleteOneTask(request, task_id, project_id):
    task = Task.objects.get(pk=task_id)
    task.delete()
    return redirect('getOneProject', id=project_id)

def ajoutDevToTask(request, task_id, project_id):
    rel_dev_task = AssDev_Task()
    rel_dev_task.id_task = Task.objects.get(pk=task_id)
    id_dev = request.POST.get('dev_id')
    rel_dev_task.id_Developer = Developer.objects.get(pk=id_dev)
    rel_dev_task.save()
    return redirect('getOneTask', task_id=task_id, project_id=project_id) 

def deleteDevFromTask(request, task_id, dev_id, project_id):
    AssDev_Task.objects.filter(id_task=task_id, id_Developer=dev_id).delete()
    return redirect('getOneTask', task_id=task_id, project_id=project_id) 

def changeTaskStatus(request, task_id, project_id):
    task = Task.objects.get(pk=task_id)
    task.status = StatusChoice.validee
    task.save()
    return redirect('getOneTask', task_id=task_id, project_id=project_id) 

def allReportOfTask(request, task_id, project_id):
    task = Task.objects.get(pk=task_id)
    print(task.reports.all)
    context = {
        "task": task,
        'project_id': project_id
    }
    return render(request, 'planificateur/allReportsOfTask.html', context)

def ajoutReportToTask(request, task_id, project_id):
    if(request.method == "POST"):
        formReport=ReportForm(request.POST)
        if formReport.is_valid():
            formReport.save()
            task = Task.objects.get(pk=task_id)
            task.stateOfProgress = request.POST.get("pourcentage_avancement")
            task.save()
            assReportTask = AssReport_Task()
            assReportTask.id_report = formReport.instance
            assReportTask.id_task = task
            assReportTask.save()
            return redirect('allReportOfTask', task_id=task_id, project_id=project_id)
    else:
        formReport = ReportForm
        formStatus = StatusForm
        task = Task.objects.get(pk=task_id)
        context = {
            'formReport': formReport,
            'task': task,
            'formStatus': formStatus,
            'project_id': project_id
        }
        return render(request, 'planificateur/form_report.html', context)

def deleteReport(request, task_id, report_id, project_id):
    Report.objects.filter(id=report_id).delete()
    return redirect('allReportOfTask', task_id=task_id, project_id=project_id) 

def login(request):
    if request.method == 'POST':
        devId = request.POST['developer_id']
        developer = Developer.objects.get(id=devId)
        settings.USER_ID = developer.id
        return redirect('profil')
    else:
        try:
            developer_list = Developer.objects.all()
            context = { 'developer_list': developer_list, 'userConnected': userConnected()}
        except Developer.DoesNotExist:
            raise Http404("Error: No developer found")
    return render(request, 'planificateur/login.html', context)

def createDeveloper(request):
    if(request.method == "POST"):
        formDev=CreateDevForm(request.POST)
        if formDev.is_valid():
            formDev.save()
            return redirect('profil')
    else:
        formDev = CreateDevForm()
        context = {
            'formCreateDev': formDev,
            'userConnected': userConnected()
        }
        return render(request, 'planificateur/form_createDev.html', context)

def profil(request):
    if settings.USER_ID:
        devId = settings.USER_ID
        developer = Developer.objects.get(id=devId)
        if request.method == 'POST':
            if request.POST['isSick'] == 'sick':
                developer.isSickLeave = True
            elif request.POST['isSick'] == 'notSick':
                developer.isSickLeave = False
            developer.save()
        context = {'developer': developer, 'userConnected': userConnected()}
        return render(request, 'planificateur/profil.html', context)
    else:
        return redirect('login')

# Project
def listProject(request):
    projects = Project.objects.all()
    context = {'projects': projects, 'userConnected': userConnected()}
    return render(request, 'planificateur/project/list.html', context)

def addProject(request):
    if(request.method == "POST"):
        form=ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listProject')
    else:
        form = ProjectForm
        context = {
            'form': form,
            'userConnected': userConnected()
        }
        return render(request, 'planificateur/project/form.html', context)
    
def updateProject(request, id):
    isTheProjectManager = False
    project = Project.objects.get(id=id)
    user = userConnected()
    if settings.USER_ID:
        isTheProjectManager = project.id_projectManager == user
    if(request.method == "POST"):
        formData=ProjectForm(request.POST)
        if formData.is_valid():
            if isTheProjectManager:
                project = formData
            else:
                formData.id_projectManager = project.id_projectManager
                project = formData
            project.save()
            return redirect('getOneProject', id=formData.instance.id)
    else:
        formData = ProjectForm(instance=project)
        context = {
            'form': formData,
            'id': id,
            'isTheProjectManager': isTheProjectManager,
            'userConnected': user
        }
        return render(request, 'planificateur/project/form.html', context)
    
def getOneProject(request, id): 
    assProject_Tasks = AssProject_Task.objects.filter(id_project = id)
    tasks = []
    for ass in assProject_Tasks :
        tasks.append(ass.id_task)
    project = Project.objects.get(id = id)
    context = {
        'project': project,
        'tasks': tasks,
        'userConnected': userConnected()
    }
    return render(request, 'planificateur/project/project.html', context)


def handle_not_found(request, exception):
    return render(request, 'planificateur/404.html', status=404)

def handle_internal_server_error(request):
    return render(request, 'planificateur/500.html', status=500)

def userConnected():
    if settings.USER_ID:
        return Developer.objects.get(id=settings.USER_ID)
    else:
        return False
