# Generated by Django 4.1.7 on 2023-05-15 00:55

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0024_alter_category_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='route',
            name='color',
            field=colorfield.fields.ColorField(default='#FF0000', image_field=None, max_length=18, samples=None, verbose_name='Cor da rota'),
        ),
    ]
