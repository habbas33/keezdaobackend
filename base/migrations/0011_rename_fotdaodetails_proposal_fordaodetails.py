# Generated by Django 4.1 on 2022-08-14 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_proposal'),
    ]

    operations = [
        migrations.RenameField(
            model_name='proposal',
            old_name='fotDaoDetails',
            new_name='forDaoDetails',
        ),
    ]
