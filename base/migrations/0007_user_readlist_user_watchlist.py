# Generated by Django 4.0.5 on 2022-09-04 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_rename_diplay_name_user_display_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='readlist',
            field=models.ManyToManyField(to='base.manga'),
        ),
        migrations.AddField(
            model_name='user',
            name='watchlist',
            field=models.ManyToManyField(to='base.anime'),
        ),
    ]