# Generated by Django 3.1.4 on 2021-03-23 21:47

import apps.homework.helpers
import apps.homework.storage
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
        ('teaching', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', model_utils.fields.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, max_length=255, populate_from='title')),
                ('description', models.TextField(blank=True)),
                ('max_score', models.PositiveSmallIntegerField()),
                ('tests', models.FileField(max_length=255, storage=apps.homework.storage.OverwriteStorage(), upload_to=apps.homework.helpers.get_tests_path)),
                ('min_upload_size', models.PositiveIntegerField(default=30, verbose_name='Minimal byte size')),
                ('max_upload_size', models.PositiveIntegerField(default=5000, verbose_name='Maximal byte size')),
                ('timeout', models.PositiveSmallIntegerField(default=10, verbose_name='Timeout in seconds')),
                ('programming_language', models.CharField(choices=[('py', 'Python'), ('r', 'R')], max_length=2)),
                ('rated', models.BooleanField(default=True, verbose_name='Graded')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teaching.lesson')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='ExerciseResource',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', model_utils.fields.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('file', models.FileField(max_length=255, storage=apps.homework.storage.OverwriteStorage(), upload_to=apps.homework.helpers.get_exercise_rsc_path)),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='resources', to='homework.exercise')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', model_utils.fields.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('file', models.FileField(max_length=255, upload_to=apps.homework.helpers.get_submission_path)),
                ('file_hash', models.CharField(max_length=40)),
                ('score', models.PositiveSmallIntegerField(default=0)),
                ('output', models.TextField(blank=True)),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='homework.exercise')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('file_hash', 'user', 'exercise')},
            },
        ),
    ]
