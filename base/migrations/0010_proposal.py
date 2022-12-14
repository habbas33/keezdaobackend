# Generated by Django 4.1 on 2022-08-14 09:04

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_alter_daos_createdat'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proposal',
            fields=[
                ('proposalType', models.CharField(max_length=50)),
                ('proposalName', models.CharField(max_length=50)),
                ('categories', jsonfield.fields.JSONField(null=True)),
                ('description', models.TextField()),
                ('proposalDetails', jsonfield.fields.JSONField(null=True)),
                ('fotDaoDetails', jsonfield.fields.JSONField(null=True)),
                ('CID', jsonfield.fields.JSONField(null=True)),
                ('url', jsonfield.fields.JSONField(null=True)),
                ('creator', jsonfield.fields.JSONField(null=True)),
                ('identifier', jsonfield.fields.JSONField(null=True)),
                ('createdAt', jsonfield.fields.JSONField(null=True)),
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
            ],
        ),
    ]
