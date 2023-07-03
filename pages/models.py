from django.db import models
from django.contrib.auth.models import User
class Product(models.Model):
    product_name=models.CharField(max_length=100,verbose_name="name")
    product_desc=models.TextField(verbose_name="description")
    product_price=models.DecimalField(max_digits=5,decimal_places=2,verbose_name="Price")
    product_cost=models.DecimalField(max_digits=5,decimal_places=2,verbose_name="Cost")
    product_created=models.DateTimeField(verbose_name="Created At")
    product_Size=models.CharField(max_length=100,blank=True,null=True)
    product_color=models.CharField(max_length=100,blank=True,null=True)
    product_material=models.CharField(max_length=100,blank=True,null=True)
    product_image=models.ImageField(upload_to='product/' ,verbose_name="image")
    product_brand_name=models.CharField(max_length=100,blank=True,null=True)
    def __str__(self):
        return self.product_name
class Category(models.Model):
    Category_name=models.CharField(max_length=100,verbose_name="name")
    Category_parent=models.ForeignKey('self',on_delete=models.CASCADE,blank=True,null=True,verbose_name='general product')
    Category_desc=models.TextField(verbose_name='description')
    Category_image=models.ImageField(upload_to='categories/')
    def __str__(self):
        return self.Category_name
class Product_Alternative(models.Model):
    main_Product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name="main_product",verbose_name="Main Product")
    alternative_product=models.ManyToManyField(Product,related_name="alternative_product",verbose_name="Alternative Product")
    def __str__(self):
        return self.main_Product
class Product_accessories(models.Model):
    main_accessory=models.ForeignKey(Product,on_delete=models.CASCADE,related_name="main_accessory",verbose_name="Main accessory")
    alternative_accessory=models.ManyToManyField(Product,related_name="alternative_accessory",verbose_name="Alternative accessory")
    def __str__(self):
        return self.main_accessory
class user_profile(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    def __str__(self):
        return self.email