# Generated by Django 3.2.22 on 2023-11-05 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_remove_document_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='title',
        ),
        migrations.AlterField(
            model_name='document',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]