# Generated by Django 2.2.5 on 2020-05-21 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_auto_20200521_0146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email_secret',
            field=models.CharField(blank=True, default='25b23261191b40c19236', max_length=20),
        ),
    ]
