# Generated by Django 3.2.22 on 2023-11-04 04:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='author',
        ),
    ]