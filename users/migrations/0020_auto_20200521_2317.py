# Generated by Django 2.2.5 on 2020-05-21 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_auto_20200521_2313'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='avatar',
        ),
        migrations.AlterField(
            model_name='user',
            name='email_secret',
            field=models.CharField(blank=True, default='f621cca5ff534ad4aca7', max_length=20),
        ),
    ]
