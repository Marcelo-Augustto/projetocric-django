# Generated by Django 4.1.7 on 2023-05-26 23:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0007_alter_routepath_concentration'),
    ]

    operations = [
        migrations.CreateModel(
            name='Warning',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Título')),
                ('content', models.CharField(max_length=500, verbose_name='Conteúdo')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event', to='event.event')),
            ],
        ),
    ]