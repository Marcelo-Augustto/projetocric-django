# Generated by Django 4.1.7 on 2023-05-03 16:50

import cities.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0023_rename_banner_photo_city_banner_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.FileField(upload_to='cities/categories/photos/%Y/%m/%d', validators=[cities.validators.validate_file_extension_category]),
        ),
    ]
