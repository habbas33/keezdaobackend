# Generated by Django 4.1 on 2022-11-04 06:09

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_vote'),
    ]

    operations = [
        migrations.AddField(
            model_name='daos',
            name='link',
            field=jsonfield.fields.JSONField(null=True),
        ),
    ]
