# Generated by Django 3.2.4 on 2021-06-06 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CoreConfig',
            new_name='AppConfiguration',
        ),
    ]
