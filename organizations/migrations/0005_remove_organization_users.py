# Generated by Django 2.2.5 on 2020-05-19 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0004_auto_20200518_2151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='users',
        ),
    ]
