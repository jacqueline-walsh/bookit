# Generated by Django 2.2.6 on 2019-11-18 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0002_remove_author_hire_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/'),
        ),
    ]
