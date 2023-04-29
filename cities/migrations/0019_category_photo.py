# Generated by Django 4.2 on 2023-04-28 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0018_remove_category_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='photo',
            field=models.FileField(default=None, upload_to='', verbose_name='cities/categories/photos/%Y/%m/%d'),
        ),
    ]