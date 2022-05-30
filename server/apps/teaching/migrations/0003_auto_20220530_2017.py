# Generated by Django 3.2.13 on 2022-05-30 18:17

import apps.teaching.helpers
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teaching', '0002_auto_20210404_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lectureresource',
            name='file',
            field=models.FileField(max_length=255, upload_to=apps.teaching.helpers.get_lecture_rsc_path),
        ),
        migrations.AlterField(
            model_name='lessonresource',
            name='file',
            field=models.FileField(max_length=255, upload_to=apps.teaching.helpers.get_lesson_rsc_path),
        ),
    ]
