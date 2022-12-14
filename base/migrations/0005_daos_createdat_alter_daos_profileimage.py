# Generated by Django 4.1 on 2022-08-08 12:30

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_daos_profileimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='daos',
            name='createdAt',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='daos',
            name='profileImage',
            field=jsonfield.fields.JSONField(null=True),
        ),
    ]
