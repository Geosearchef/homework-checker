# Generated by Django 3.2.13 on 2022-05-30 18:17

import apps.homework.helpers
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0006_auto_20210423_0329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='tests',
            field=models.FileField(max_length=255, upload_to=apps.homework.helpers.get_tests_path),
        ),
        migrations.AlterField(
            model_name='exerciseresource',
            name='file',
            field=models.FileField(max_length=255, upload_to=apps.homework.helpers.get_exercise_rsc_path),
        ),
    ]