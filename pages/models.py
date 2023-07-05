from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db.models.signals import post_save
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
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,blank=True,null=True)
    first_name=models.CharField(max_length=100,blank=True,null=True)
    last_name=models.CharField(max_length=100,blank=True,null=True)
    email=models.CharField(max_length=100,blank=True,null=True)
    image=models.ImageField(upload_to='user_photo/',blank=True,null=True)
    phone_number=models.CharField(max_length=100,blank=True,null=True)
    state=models.CharField(max_length=100,blank=True,null=True)
    address=models.CharField(max_length=100,blank=True,null=True)
    street=models.CharField(max_length=100,blank=True,null=True)
    country=models.CharField(max_length=100,blank=True,null=True)
    city=models.CharField(max_length=100,blank=True,null=True)
    create_at=models.DateTimeField(auto_now_add=True)
    slug=models.SlugField(blank=True,null=True)
    def save(self,*args,**kwarg):
        if not self.slug:
            self.slug=slugify(self.user.username)
        super(Profile,self).save(*args,**kwarg)
    def __str__(self):
        return self.slug
def create_profile(sender,**kwargs):
    if kwargs['created']:
        user_profile=Profile.objects.create(user=kwargs['instance'])
post_save.connect(create_profile,sender=User)

class order_DB(models.Model):
    order=models.ForeignKey(User,on_delete=models.CASCADE)
    total_orders=models.IntegerField(default=0)
    order_name=models.CharField(max_length=100)
    order_desc=models.TextField(null=True,blank=True)
    order_quantity=models.IntegerField(default=0)
    order_price=models.FloatField(default=0.0)
    order_image=models.ImageField(upload_to='orders/',null=True,blank=True)
    order_created=models.DateTimeField(auto_now_add=True)

