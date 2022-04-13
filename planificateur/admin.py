from django.contrib import admin
from planificateur.models import *

# Register your models here.
admin.site.register(Task)
admin.site.register(Developer)
admin.site.register(AssDev_Task)
admin.site.register(AssProject_Dev)
admin.site.register(AssProject_Task)
admin.site.register(AssReport_Task)
admin.site.register(Project)
admin.site.register(Evaluator)
admin.site.register(Report)
