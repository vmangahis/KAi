# Generated by Django 4.0.5 on 2022-12-03 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0017_remove_anime_genre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anime',
            name='watchers',
        ),
    ]
