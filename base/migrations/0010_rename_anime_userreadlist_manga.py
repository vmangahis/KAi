# Generated by Django 4.0.5 on 2022-10-18 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_readliststatus_userreadlist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userreadlist',
            old_name='anime',
            new_name='manga',
        ),
    ]