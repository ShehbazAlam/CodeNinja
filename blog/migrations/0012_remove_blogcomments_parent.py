# Generated by Django 4.1.2 on 2023-01-10 07:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_blog_tags_blogcomments_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogcomments',
            name='parent',
        ),
    ]
