# Generated by Django 3.2.9 on 2022-01-02 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_photos_caption'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photos',
            name='likes',
            field=models.IntegerField(default=0, null=True),
        ),
    ]