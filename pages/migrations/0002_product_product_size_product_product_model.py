# Generated by Django 4.1.7 on 2023-07-03 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_Size',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='product_model',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
