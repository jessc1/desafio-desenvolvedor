# Generated by Django 5.1 on 2024-09-06 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileupload', '0002_alter_file_upload_date'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='file',
            name='fileupload__name_8bd4da_idx',
        ),
        migrations.AddIndex(
            model_name='file',
            index=models.Index(fields=['-name', 'RptDt'], name='fileupload__name_29b6d7_idx'),
        ),
    ]