# Generated by Django 3.1.7 on 2023-05-05 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0004_auto_20230430_1905'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tareamayo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('completado', models.BooleanField(default=False)),
            ],
        ),
    ]