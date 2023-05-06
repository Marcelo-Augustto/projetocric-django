# Generated by Django 4.2 on 2023-05-03 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0009_event_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='lat',
            field=models.CharField(blank=True, default='-29.95', max_length=20, null=True, verbose_name='Latitute de Mapa'),
        ),
        migrations.AddField(
            model_name='event',
            name='lng',
            field=models.CharField(blank=True, default='-51.64', max_length=20, null=True, verbose_name='Longitude do Mapa'),
        ),
    ]
