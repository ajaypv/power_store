# Generated by Django 3.2.9 on 2021-12-29 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photos',
            name='caption',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
    ]
