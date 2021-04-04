# Generated by Django 3.1.7 on 2021-04-04 13:21

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teaching', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='slug',
            field=autoslug.fields.AutoSlugField(always_update=True, editable=False, max_length=255, populate_from='title', unique=True),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='slug',
            field=autoslug.fields.AutoSlugField(always_update=True, editable=False, max_length=255, populate_from='title'),
        ),
    ]
