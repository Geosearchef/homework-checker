# Generated by Django 3.1.2 on 2020-11-09 15:29

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
            name='Lecture',
            fields=[
                ('start', models.DateTimeField(blank=True, null=True, verbose_name='start')),
                ('end', models.DateTimeField(blank=True, null=True, verbose_name='end')),
                ('id', model_utils.fields.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='Titel')),
                ('description', models.TextField(blank=True, verbose_name='Beschreibung')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique=True)),
                ('participants', models.ManyToManyField(related_name='enrolled_lectures', to=settings.AUTH_USER_MODEL, verbose_name='Teilnehmer')),
            ],
            options={
                'verbose_name': 'Vorlesung',
                'verbose_name_plural': 'Vorlesungen',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('start', models.DateTimeField(blank=True, null=True, verbose_name='start')),
                ('end', models.DateTimeField(blank=True, null=True, verbose_name='end')),
                ('id', model_utils.fields.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100, verbose_name='Titel')),
                ('description', models.TextField(blank=True, verbose_name='Beschreibung')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title')),
                ('lecture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='teaching.lecture', verbose_name='Vorlesung')),
            ],
            options={
                'verbose_name': 'Lektion',
                'verbose_name_plural': 'Lektionen',
                'ordering': ['title'],
                'unique_together': {('lecture', 'title')},
            },
        ),
        migrations.CreateModel(
            name='LessonResource',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', model_utils.fields.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100, verbose_name='Titel')),
                ('file', models.FileField(upload_to=apps.teaching.helpers.get_lesson_rsc_path)),
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='teaching.lesson')),
            ],
            options={
                'verbose_name': 'Lektionsmaterial',
                'verbose_name_plural': 'Lektionsmaterialen',
                'unique_together': {('entity', 'title')},
            },
        ),
        migrations.CreateModel(
            name='LectureResource',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', model_utils.fields.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100, verbose_name='Titel')),
                ('file', models.FileField(upload_to=apps.teaching.helpers.get_lecture_rsc_path)),
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='teaching.lecture')),
            ],
            options={
                'verbose_name': 'Vorlesungsmaterial',
                'verbose_name_plural': 'Vorlesungmaterialien',
                'unique_together': {('entity', 'title')},
            },
        ),
    ]