# Generated by Django 3.2.18 on 2023-04-05 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movies',
            name='genres',
        ),
        migrations.AddField(
            model_name='movies',
            name='genres',
            field=models.ManyToManyField(null=True, to='myapp.Genres'),
        ),
    ]
