# Generated by Django 4.1.7 on 2023-03-27 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='polilyne',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]