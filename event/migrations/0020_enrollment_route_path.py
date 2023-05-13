# Generated by Django 4.1.7 on 2023-05-13 01:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0019_routepath'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrollment',
            name='route_path',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='event.routepath', verbose_name='Nome do Trajeto'),
            preserve_default=False,
        ),
    ]