# Generated by Django 3.1.4 on 2021-03-14 14:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import model_utils.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('teaching', '0016_auto_20201219_0121'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gradingscale',
            options={},
        ),
        migrations.AlterModelOptions(
            name='lecture',
            options={'ordering': ['title']},
        ),
        migrations.AlterModelOptions(
            name='lectureresource',
            options={},
        ),
        migrations.AlterModelOptions(
            name='lesson',
            options={},
        ),
        migrations.AlterModelOptions(
            name='lessonresource',
            options={'verbose_name': 'Lesson Resource', 'verbose_name_plural': 'Lesson Resources'},
        ),
        migrations.AlterField(
            model_name='gradingscale',
            name='grade_1_0',
            field=models.PositiveIntegerField(verbose_name='Points needed to reach 1.0'),
        ),
        migrations.AlterField(
            model_name='gradingscale',
            name='grade_1_3',
            field=models.PositiveIntegerField(verbose_name='Points needed to reach 1.3'),
        ),
        migrations.AlterField(
            model_name='gradingscale',
            name='grade_1_7',
            field=models.PositiveIntegerField(verbose_name='Points needed to reach 1.7'),
        ),
        migrations.AlterField(
            model_name='gradingscale',
            name='grade_2_0',
            field=models.PositiveIntegerField(verbose_name='Points needed to reach 2.0'),
        ),
        migrations.AlterField(
            model_name='gradingscale',
            name='grade_2_3',
            field=models.PositiveIntegerField(verbose_name='Points needed to reach 2.3'),
        ),
        migrations.AlterField(
            model_name='gradingscale',
            name='grade_2_7',
            field=models.PositiveIntegerField(verbose_name='Points needed to reach 2.7'),
        ),
        migrations.AlterField(
            model_name='gradingscale',
            name='grade_3_0',
            field=models.PositiveIntegerField(verbose_name='Points needed to reach 3.0'),
        ),
        migrations.AlterField(
            model_name='gradingscale',
            name='grade_3_3',
            field=models.PositiveIntegerField(verbose_name='Points needed to reach 3.3'),
        ),
        migrations.AlterField(
            model_name='gradingscale',
            name='grade_3_7',
            field=models.PositiveIntegerField(verbose_name='Points needed to reach 3.7'),
        ),
        migrations.AlterField(
            model_name='gradingscale',
            name='grade_4_0',
            field=models.PositiveIntegerField(verbose_name='Points needed to reach 4.0'),
        ),
        migrations.AlterField(
            model_name='gradingscale',
            name='grade_5_0',
            field=models.PositiveIntegerField(default=0, verbose_name='Points needed to reach 5.0'),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='grading_scale',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='teaching.gradingscale'),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='participants',
            field=models.ManyToManyField(related_name='enrolled_lectures', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='title',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='lecture',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='teaching.lecture'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='title',
            field=models.CharField(max_length=100),
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
    ]