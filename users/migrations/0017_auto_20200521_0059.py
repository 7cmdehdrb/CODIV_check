# Generated by Django 2.2.5 on 2020-05-20 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_auto_20200521_0059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email_secret',
            field=models.CharField(blank=True, default='68ba2e7ce3f4418b971e', max_length=20),
        ),
    ]
