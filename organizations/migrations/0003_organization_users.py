# Generated by Django 2.2.5 on 2020-05-18 08:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('organizations', '0002_organization_master'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='users',
            field=models.ManyToManyField(related_name='users', to=settings.AUTH_USER_MODEL),
        ),
    ]
