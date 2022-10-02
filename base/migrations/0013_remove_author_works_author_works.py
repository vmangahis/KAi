# Generated by Django 4.0.5 on 2022-09-23 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_author_alter_manga_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='works',
        ),
        migrations.AddField(
            model_name='author',
            name='works',
            field=models.ManyToManyField(blank=True, null=True, related_name='author_work', to='base.manga'),
        ),
    ]