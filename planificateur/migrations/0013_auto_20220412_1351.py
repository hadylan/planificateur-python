# Generated by Django 3.2.9 on 2022-04-12 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planificateur', '0012_task_reports'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='deleveryDate',
        ),
        migrations.AddField(
            model_name='project',
            name='deliveryDate',
            field=models.DateField(blank=True, null=True),
        ),
    ]