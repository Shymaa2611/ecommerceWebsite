# Generated by Django 4.2.3 on 2023-07-25 10:23

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100, verbose_name='name')),
                ('product_desc', models.TextField(verbose_name='description')),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Price')),
                ('product_cost', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Cost')),
                ('product_created', models.DateTimeField(verbose_name='Created At')),
                ('product_Size', models.CharField(blank=True, max_length=100, null=True)),
                ('product_color', models.CharField(blank=True, max_length=100, null=True)),
                ('product_material', models.CharField(blank=True, max_length=100, null=True)),
                ('product_image', models.ImageField(upload_to='product/', verbose_name='image')),
                ('product_brand_name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='user_photo/')),
                ('phone_number', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('street', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product_Alternative',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alternative_product', models.ManyToManyField(related_name='alternative_product', to='pages.product', verbose_name='Alternative Product')),
                ('main_Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='main_product', to='pages.product', verbose_name='Main Product')),
            ],
        ),
        migrations.CreateModel(
            name='Product_accessories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alternative_accessory', models.ManyToManyField(related_name='alternative_accessory', to='pages.product', verbose_name='Alternative accessory')),
                ('main_accessory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='main_accessory', to='pages.product', verbose_name='Main accessory')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category_name', models.CharField(max_length=100, verbose_name='name')),
                ('Category_desc', models.TextField(verbose_name='description')),
                ('Category_image', models.ImageField(upload_to='categories/')),
                ('Category_parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.category', verbose_name='general product')),
            ],
        ),
        migrations.CreateModel(
            name='Wish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('love', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'product')},
                'index_together': {('user', 'product')},
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stars', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'product')},
                'index_together': {('user', 'product')},
            },
        ),
    ]
