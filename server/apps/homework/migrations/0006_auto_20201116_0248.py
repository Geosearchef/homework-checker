# Generated by Django 3.1.2 on 2020-11-16 01:48

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('homework', '0005_auto_20201116_0248'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='submission',
            unique_together={('file_hash', 'user')},
        ),
    ]
