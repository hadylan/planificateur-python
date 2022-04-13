from django.urls import path
from planificateur import views
urlpatterns = [
    path('', views.index,name='index'),
    path('projects', views.listProject, name='listProject'),
    path('projects/add', views.addProject, name='addProject'),
    path('projects/<int:id>', views.getOneProject,name='getOneProject'),
    path('projects/<int:id>/update', views.updateProject, name='updateProject'),
    
    path('projects/<int:project_id>/task/<int:task_id>', views.getOneTask,name='getOneTask'),
    path('projects/<int:project_id>/task/add', views.addTask,name='addTask'),
    path('projects/<int:project_id>/task/<int:task_id>/update', views.updateTask,name='updateTask'),
    path('projects/<int:project_id>/task/<int:task_id>/reports/add', views.ajoutReportToTask,name='ajoutReportToTask'),
    path('projects/<int:project_id>/task/<int:task_id>/reports', views.allReportOfTask,name='allReportOfTask'),
    path('projects/<int:project_id>/task/<int:task_id>/reports/<int:report_id>/delete', views.deleteReport,name='deleteReport'),
    path('projects/<int:project_id>/task/delete/<int:task_id>', views.deleteOneTask,name='deleteOneTask'),
    path('projects/<int:project_id>/task/<int:task_id>/dev/<int:dev_id>/delete', views.deleteDevFromTask,name='deleteDevFromTask'),
    path('projects/<int:project_id>/task/<int:task_id>/dev/add', views.ajoutDevToTask,name='ajoutDevToTask'),
    path('projects/<int:project_id>/task/<int:task_id>/changeStatus', views.changeTaskStatus,name='changeTaskStatus'),
    path('login/', views.login, name="login"),
    path('createDev/', views.createDeveloper, name="createDev"),
    path('profil/', views.profil, name="profil")
]