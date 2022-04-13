# Generated by Django 3.2.9 on 2022-04-04 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planificateur', '0004_rename_fields_task_developers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Faible'), (1, 'Normale'), (2, 'Haute')], default=1),
        ),
    ]