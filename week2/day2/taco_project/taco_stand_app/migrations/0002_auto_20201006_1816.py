# Generated by Django 2.2.4 on 2020-10-06 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taco_stand_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taco',
            name='image_url',
            field=models.CharField(max_length=255),
        ),
    ]
