# Generated by Django 2.2.6 on 2019-10-13 12:06

import datetime
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
                ('name', models.CharField(max_length=200)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('description', models.TextField(blank=True)),
                ('is_author_of_month', models.BooleanField(default=False)),
                ('hire_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]