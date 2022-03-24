# Generated by Django 2.2.26 on 2022-03-16 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venyou_app', '0002_venue_name_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='banner_picture',
            field=models.ImageField(default=0, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='venue',
            name='latitude',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='venue',
            name='longitude',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]