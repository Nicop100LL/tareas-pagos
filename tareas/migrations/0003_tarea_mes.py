# Generated by Django 3.1.7 on 2023-04-28 02:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0002_mes'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarea',
            name='mes',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tareas.mes'),
        ),
    ]
