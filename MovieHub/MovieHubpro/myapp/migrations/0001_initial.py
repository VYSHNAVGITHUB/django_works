# Generated by Django 4.1.7 on 2023-04-10 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=200, unique=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('year', models.CharField(max_length=200)),
                ('language', models.CharField(choices=[('malayalam', 'malayalam'), ('telungu', 'telungu'), ('tamil', 'tamil'), ('hindi', 'hindi'), ('english', 'english')], default='malayalam', max_length=200)),
                ('runtime', models.FloatField()),
                ('poster_image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('description', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
