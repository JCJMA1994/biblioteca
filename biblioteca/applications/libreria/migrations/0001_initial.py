# Generated by Django 3.1.7 on 2021-03-21 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='Nombres')),
                ('nationality', models.CharField(blank=True, max_length=100, verbose_name='Nacionalidad')),
            ],
        ),
    ]
