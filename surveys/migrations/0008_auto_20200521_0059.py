# Generated by Django 2.2.5 on 2020-05-20 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0007_auto_20200520_0225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='date',
            field=models.DateField(default='2020-05-21'),
        ),
    ]
