# Generated by Django 4.1.7 on 2023-05-13 01:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0017_enrollment_email_enrollment_social_network'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enrollment',
            name='route',
        ),
    ]