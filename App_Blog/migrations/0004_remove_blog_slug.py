# Generated by Django 4.0.6 on 2022-08-22 07:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_Blog', '0003_alter_blog_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='slug',
        ),
    ]
