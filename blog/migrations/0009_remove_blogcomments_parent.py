# Generated by Django 4.1.2 on 2023-01-03 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_blog_author_blog_sno'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogcomments',
            name='parent',
        ),
    ]
