# Generated by Django 4.1.7 on 2023-04-10 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0006_route_active_alter_city_banner_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='id_map',
        ),
    ]