from email.policy import default
from django.db import models
import django
from datetime import timezone,timedelta,datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import gettext_lazy as _

# Create your models here.
class StatusChoice(models.TextChoices):
    planifiee = 'Planifie', _('Planifié')
    enCours = 'En cours', _('En cours')
    realisee = 'Realise', _('Réalisé')
    enPause = 'En pause', _('En pause')
    validee = 'Valide', _('Validé')
    livre = 'Livre', _('Livré')

class PriorityChoice(models.IntegerChoices):
    faible = 0, _('Faible')
    normale = 1, _('Normale')
    haute = 2, _('Haute')
    
class Developer(models.Model):
    id = models.BigAutoField(primary_key=True) #clé primaire de l'entité autoincrémentée
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    isSickLeave = models.BooleanField(default=False)

    def __str__(self):
        return self.firstname + ' ' + self.lastname
    
    
class Project(models.Model):
    status = models.CharField(
        choices=StatusChoice.choices,
        default=StatusChoice.enCours,
        max_length=200
        )
    deliveryDate = models.DateField(null=True, blank=True)
    startingDate = models.DateField(default=django.utils.timezone.now, null=True)
    stateOfProgress= models.PositiveSmallIntegerField(default=0)
    desc = models.CharField(max_length=250)
    name = models.CharField(max_length=50, default="")
    id_projectManager = models.ForeignKey(Developer, on_delete=models.DO_NOTHING)

class Report(models.Model):
    id = models.BigAutoField(primary_key=True) #clé primaire de l'entité autoincrémentée
    content = models.TextField()
    date = models.DateField(default=django.utils.timezone.now)

class Task(models.Model):
    id = models.BigAutoField(primary_key=True) #clé primaire de l'entité autoincrémentée
    desc = models.CharField(max_length=250)
    priority = models.PositiveSmallIntegerField(
        choices=PriorityChoice.choices,
        default=PriorityChoice.normale
    )
    duree = models.PositiveIntegerField()
    startingDate = models.DateField(default=django.utils.timezone.now)
    stateOfProgress= models.PositiveSmallIntegerField(default=0)
    status = models.CharField(
        choices=StatusChoice.choices,
        default=StatusChoice.enCours,
        max_length=200
        )
    developers = models.ManyToManyField(Developer, through='AssDev_Task')
    reports = models.ManyToManyField(Report, through='AssReport_Task')

class AssDev_Task(models.Model):
    id_task= models.ForeignKey(Task, on_delete=models.CASCADE)
    id_Developer = models.ForeignKey(Developer, on_delete=models.CASCADE)
    
class AssProject_Dev(models.Model):
    id_project = models.ForeignKey(Project, on_delete=models.CASCADE)
    id_developer = models.ForeignKey(Developer, on_delete=models.CASCADE)
    
class AssProject_Task(models.Model):
    id_project = models.ForeignKey(Project, on_delete=models.CASCADE)
    id_task = models.ForeignKey(Task, on_delete=models.CASCADE)

class AssReport_Task(models.Model):
    id_report = models.ForeignKey(Report, on_delete=models.CASCADE)
    id_task = models.ForeignKey(Task, on_delete=models.CASCADE)

class Evaluator(models.Model):
    id_task= models.ForeignKey(Task, on_delete=models.CASCADE)
    id_Developer = models.ForeignKey(Developer, on_delete=models.CASCADE)
    


