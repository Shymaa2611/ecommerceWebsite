# Generated by Django 4.2.3 on 2023-07-25 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_remove_product_product_created'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-create_at']},
        ),
    ]
