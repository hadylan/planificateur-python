# Generated by Django 3.2.9 on 2022-04-08 22:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planificateur', '0010_auto_20220406_2344'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='project',
        ),
    ]
