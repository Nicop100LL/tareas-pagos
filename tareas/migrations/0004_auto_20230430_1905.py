# Generated by Django 3.1.7 on 2023-04-30 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0003_tarea_mes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tarea1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('completado', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Tarea2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('completado', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='tarea',
            name='mes',
        ),
        migrations.DeleteModel(
            name='Mes',
        ),
    ]
