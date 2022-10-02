# Generated by Django 4.0.5 on 2022-10-02 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0018_anime_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='manga',
            name='large_image',
            field=models.URLField(default='https://picsum.photos/seed/picsum/500/500'),
        ),
        migrations.AddField(
            model_name='manga',
            name='thumbnail',
            field=models.URLField(default='https://picsum.photos/seed/picsum/300/500'),
        ),
    ]
