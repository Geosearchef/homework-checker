# Generated by Django 3.1.2 on 2020-11-23 19:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teaching', '0009_auto_20201123_2016'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lesson',
            options={'verbose_name': 'Lektion', 'verbose_name_plural': 'Lektionen'},
        ),
        migrations.AlterUniqueTogether(
            name='lesson',
            unique_together={('lecture', 'title')},
        ),
    ]