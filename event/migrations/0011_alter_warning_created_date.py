# Generated by Django 4.1.7 on 2023-05-27 00:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0010_warning_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warning',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data de criação'),
        ),
    ]
