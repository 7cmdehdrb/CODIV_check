# Generated by Django 2.2.5 on 2020-05-21 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0020_auto_20200521_2317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email_secret',
            field=models.CharField(blank=True, default='ec32c986cb5048df8c2f', max_length=20),
        ),
    ]
