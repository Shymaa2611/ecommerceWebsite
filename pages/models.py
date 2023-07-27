from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.core.validators import MaxValueValidator,MinValueValidator
from django.db.models.signals import post_save
class Brand(models.Model):
    name=models.CharField(max_length=20)
    def __str__(self):
        return self.name
class Category(models.Model):
    Category_name=models.CharField(max_length=100,verbose_name="name")
    Category_desc=models.TextField(verbose_name='description')
    Category_image=models.ImageField(upload_to='categories/')
    def __str__(self):
        return self.Category_name

class Product(models.Model):
    product_name=models.CharField(max_length=100,verbose_name="name")
    product_desc=models.TextField(verbose_name="description")
    product_price=models.DecimalField(max_digits=5,decimal_places=2,verbose_name="Price")
    product_cost=models.DecimalField(max_digits=5,decimal_places=2,verbose_name="Cost")
    product_Size=models.CharField(max_length=100,blank=True,null=True)
    product_color=models.CharField(max_length=100,blank=True,null=True)
    product_material=models.CharField(max_length=100,blank=True,null=True)
    product_image=models.ImageField(upload_to='product/' ,verbose_name="image")
    brand=models.ForeignKey(Brand,on_delete=models.Case,blank=True,null=True)
    category=models.ForeignKey(Category,on_delete=models.Case,blank=True,null=True)
    create_at=models.DateField(auto_now_add=True)
    def no_of_rating(self):
        no_ratings=Rating.objects.filter(product=self).count()
        return no_ratings
    def avg_rating(self):
        sum_ratings=0
        ratings=Rating.objects.filter(product=self)
        for rate in ratings:
            sum_ratings+=rate.stars
        if ratings==0:
           ratings=1
           return sum_ratings/ratings
    class Meta:
        ordering=['-create_at']



    def __str__(self):
        return self.product_name

class Product_Alternative(models.Model):
    main_Product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name="main_product",verbose_name="Main Product")
    alternative_product=models.ManyToManyField(Product,related_name="alternative_product",verbose_name="Alternative Product")
    def __str__(self):
        return self.main_Product.product_name

class Product_accessories(models.Model):
    main_accessory=models.ForeignKey(Product,on_delete=models.CASCADE,related_name="main_accessory",verbose_name="Main accessory")
    alternative_accessory=models.ManyToManyField(Product,related_name="alternative_accessory",verbose_name="Alternative accessory")
    def __str__(self):
        return self.main_accessory.product_name

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

class Wish(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    love=models.IntegerField(default=0,validators=[MinValueValidator(0),MaxValueValidator(1)])
    def __str__(self):
        return str(self.product.product_name)
    class Meta:
        unique_together=(('user','product'))
        index_together=(('user','product'))
class Rating(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    stars=models.IntegerField(default=0,validators=[MinValueValidator(1),MaxValueValidator(5)])
    def __str__(self):
        return str(self.product.product_name)
    class Meta:
        unique_together=(('user','product'))
        index_together=(('user','product'))



