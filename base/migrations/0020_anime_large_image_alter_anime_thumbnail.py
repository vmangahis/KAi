# Generated by Django 4.0.5 on 2022-10-02 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0019_manga_large_image_manga_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='large_image',
            field=models.URLField(default='https://picsum.photos/seed/picsum/500/500', null=True),
        ),
        migrations.AlterField(
            model_name='anime',
            name='thumbnail',
            field=models.URLField(default='https://picsum.photos/seed/picsum/300/500', null=True),
        ),
    ]