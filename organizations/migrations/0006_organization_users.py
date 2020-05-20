# Generated by Django 2.2.5 on 2020-05-20 06:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('organizations', '0005_remove_organization_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='users',
            field=models.ManyToManyField(related_name='users', to=settings.AUTH_USER_MODEL),
        ),
    ]
