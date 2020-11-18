# Generated by Django 3.1.2 on 2020-11-18 14:58

import apps.homework.helpers
import apps.homework.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0011_auto_20201118_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='tests',
            field=models.FileField(max_length=255, storage=apps.homework.storage.OverwriteStorage(), upload_to=apps.homework.helpers.get_tests_path),
        ),
        migrations.AlterField(
            model_name='exerciseresource',
            name='file',
            field=models.FileField(max_length=255, storage=apps.homework.storage.OverwriteStorage(), upload_to=apps.homework.helpers.get_exercise_rsc_path),
        ),
        migrations.AlterField(
            model_name='submission',
            name='file',
            field=models.FileField(max_length=255, upload_to=apps.homework.helpers.get_submission_path),
        ),
    ]
