# Generated by Django 2.2.26 on 2022-03-24 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venyou_app', '0004_auto_20220318_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='banner_picture',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
