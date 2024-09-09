# Generated by Django 5.1 on 2024-09-06 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileupload', '0003_remove_file_fileupload__name_8bd4da_idx_and_more'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='file',
            name='fileupload__name_29b6d7_idx',
        ),
        migrations.AddIndex(
            model_name='file',
            index=models.Index(fields=['-name', '-RptDt'], name='fileupload__name_d09d64_idx'),
        ),
    ]
