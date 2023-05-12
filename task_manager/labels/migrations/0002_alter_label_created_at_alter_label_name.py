# Generated by Django 4.2 on 2023-05-11 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labels', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='label',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Creation date'),
        ),
        migrations.AlterField(
            model_name='label',
            name='name',
            field=models.CharField(max_length=150, unique=True, verbose_name='Name'),
        ),
    ]