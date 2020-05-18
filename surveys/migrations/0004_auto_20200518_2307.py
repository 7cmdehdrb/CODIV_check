# Generated by Django 2.2.5 on 2020-05-18 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0003_auto_20200518_2248'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=80)),
                ('check', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Questions',
            },
        ),
        migrations.RemoveField(
            model_name='survey',
            name='question1',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='question2',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='question3',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='question4',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='question5',
        ),
        migrations.AddField(
            model_name='survey',
            name='questions',
            field=models.ManyToManyField(related_name='Questions', to='surveys.Questions'),
        ),
    ]
