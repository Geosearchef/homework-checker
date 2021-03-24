# Generated by Django 3.1.7 on 2021-03-24 00:11

import apps.homework.storage
import apps.teaching.helpers
import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GradingScale',
            fields=[
                ('id', model_utils.fields.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('grade_1_0', models.PositiveIntegerField(verbose_name='Points needed to reach 1.0')),
                ('grade_1_3', models.PositiveIntegerField(verbose_name='Points needed to reach 1.3')),
                ('grade_1_7', models.PositiveIntegerField(verbose_name='Points needed to reach 1.7')),
                ('grade_2_0', models.PositiveIntegerField(verbose_name='Points needed to reach 2.0')),
                ('grade_2_3', models.PositiveIntegerField(verbose_name='Points needed to reach 2.3')),
                ('grade_2_7', models.PositiveIntegerField(verbose_name='Points needed to reach 2.7')),
                ('grade_3_0', models.PositiveIntegerField(verbose_name='Points needed to reach 3.0')),
                ('grade_3_3', models.PositiveIntegerField(verbose_name='Points needed to reach 3.3')),
                ('grade_3_7', models.PositiveIntegerField(verbose_name='Points needed to reach 3.7')),
                ('grade_4_0', models.PositiveIntegerField(verbose_name='Points needed to reach 4.0')),
                ('grade_5_0', models.PositiveIntegerField(default=0, verbose_name='Points needed to reach 5.0')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('start', models.DateTimeField(blank=True, null=True, verbose_name='start')),
                ('end', models.DateTimeField(blank=True, null=True, verbose_name='end')),
                ('id', model_utils.fields.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, max_length=255, populate_from='title', unique=True)),
                ('grading_scale', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='teaching.gradingscale')),
                ('participants', models.ManyToManyField(related_name='enrolled_lectures', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('start', models.DateTimeField(blank=True, null=True, verbose_name='start')),
                ('end', models.DateTimeField(blank=True, null=True, verbose_name='end')),
                ('id', model_utils.fields.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, max_length=255, populate_from='title')),
                ('lecture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='teaching.lecture')),
            ],
            options={
                'unique_together': {('lecture', 'title')},
            },
        ),
        migrations.CreateModel(
            name='RegistrationCode',
            fields=[
                ('id', model_utils.fields.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=50, unique=True)),
                ('lecture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registration_codes', to='teaching.lecture')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LessonResource',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', model_utils.fields.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100, verbose_name='Titel')),
                ('file', models.FileField(max_length=255, storage=apps.homework.storage.OverwriteStorage(), upload_to=apps.teaching.helpers.get_lesson_rsc_path)),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resources', to='teaching.lesson')),
            ],
            options={
                'verbose_name': 'Lesson Resource',
                'verbose_name_plural': 'Lesson Resources',
                'unique_together': {('lesson', 'title')},
            },
        ),
        migrations.CreateModel(
            name='LectureResource',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', model_utils.fields.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100, verbose_name='Titel')),
                ('file', models.FileField(max_length=255, storage=apps.homework.storage.OverwriteStorage(), upload_to=apps.teaching.helpers.get_lecture_rsc_path)),
                ('lecture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resources', to='teaching.lecture')),
            ],
            options={
                'unique_together': {('lecture', 'title')},
            },
        ),
    ]
