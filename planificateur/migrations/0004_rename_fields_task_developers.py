# Generated by Django 3.2.9 on 2022-04-03 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planificateur', '0003_task_fields'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='fields',
            new_name='developers',
        ),
    ]
