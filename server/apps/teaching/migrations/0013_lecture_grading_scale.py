# Generated by Django 3.1.2 on 2020-12-18 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teaching', '0012_auto_20201218_1715'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture',
            name='grading_scale',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='teaching.gradingscale'),
        ),
    ]