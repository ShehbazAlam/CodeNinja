# Generated by Django 4.1.2 on 2023-01-07 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_alter_project_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='demolink',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='project',
            name='downlink',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
