# Generated by Django 4.2 on 2023-04-25 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0013_address_anchorpoint'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='neighboorhood',
            new_name='neighborhood',
        ),
        migrations.AddField(
            model_name='city',
            name='points',
            field=models.ManyToManyField(blank=True, null=True, to='cities.anchorpoint'),
        ),
        migrations.AlterField(
            model_name='anchorpoint',
            name='phone',
            field=models.CharField(default='(51) ', max_length=20),
        ),
        migrations.AlterField(
            model_name='category',
            name='photo',
            field=models.ImageField(upload_to='cities/categories/photos/%Y/%m/%d', verbose_name='Imagem da Categoria'),
        ),
    ]
