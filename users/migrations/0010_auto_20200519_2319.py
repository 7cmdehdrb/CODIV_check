# Generated by Django 2.2.5 on 2020-05-19 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20200519_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email_secret',
            field=models.CharField(default='15c2df409e384969985a', max_length=20),
        ),
    ]
