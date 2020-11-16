# Generated by Django 3.1.2 on 2020-11-16 09:28

import apps.homework.helpers
import apps.homework.storage
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0006_auto_20201116_0248'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='tests',
            field=models.FileField(default=1, storage=apps.homework.storage.OverwriteStorage(), upload_to=apps.homework.helpers.get_tests_path),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='ExerciseResource',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', model_utils.fields.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100, verbose_name='Titel')),
                ('file', models.FileField(storage=apps.homework.storage.OverwriteStorage(), upload_to=apps.homework.helpers.get_exercise_rsc_path)),
                ('public', models.BooleanField(default=False)),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='resources', to='homework.exercise')),
            ],
            options={
                'verbose_name': 'Vorlesungsmaterial',
                'verbose_name_plural': 'Vorlesungmaterialien',
                'unique_together': {('exercise', 'title')},
            },
        ),
    ]
