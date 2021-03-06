# Generated by Django 2.2.5 on 2020-05-18 12:51

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0003_organization_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='phone',
            field=phone_field.models.PhoneField(help_text='Contact phone number', max_length=31),
        ),
    ]
