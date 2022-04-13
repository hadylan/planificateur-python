# Generated by Django 3.2.9 on 2022-04-06 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('planificateur', '0006_task_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='id_projectManager',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.DO_NOTHING, to='planificateur.developer'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
