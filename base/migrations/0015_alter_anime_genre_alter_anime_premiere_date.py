# Generated by Django 4.0.5 on 2022-09-24 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_alter_author_works_studiocompany'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='genre',
            field=models.ManyToManyField(default=None, to='base.genre'),
        ),
        migrations.AlterField(
            model_name='anime',
            name='premiere_date',
            field=models.DateField(default=None, null=True),
        ),
    ]
