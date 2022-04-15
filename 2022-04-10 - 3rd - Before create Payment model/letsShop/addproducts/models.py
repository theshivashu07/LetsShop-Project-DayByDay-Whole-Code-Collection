from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField

class Product_Entries(models.Model):
	product_from = models.CharField(max_length=50);
	product_name = models.CharField(max_length=100);
	product_details = HTMLField(); 
	product_price = models.CharField(max_length=10);
	product_image = models.FileField(upload_to="products/", max_length=250,null=True,default=None);
	product_slug = AutoSlugField(populate_from='product_name', unique=True, null=True, default=None);
	product_create_date = models.DateTimeField(auto_now_add=True)
	product_update_date = models.DateTimeField(auto_now=True)

# This is company personal employees infor addings...
class OurAmazingTeam(models.Model):
	member_name =  models.CharField(max_length=50);
	member_role =  models.CharField(max_length=50);
	member_image = models.FileField(upload_to="products/", max_length=250,default=None, unique=True); 
	member_instagram_id = models.CharField(max_length=100, null=True, blank=True, unique=True);
	member_facebook_id = models.CharField(max_length=100, null=True, blank=True, unique=True);
	member_twitter_id = models.CharField(max_length=100, null=True, blank=True, unique=True);
	member_linkedin_id = models.CharField(max_length=100, null=True, blank=True, unique=True);
	member_github_id = models.CharField(max_length=100, null=True, blank=True, unique=True); 

# Here we manage all cart related data
class AddToCART(models.Model): 
	os_name_holder = models.CharField(max_length=50); 
	member_email = models.CharField(max_length=70); 
	member_mno = models.CharField(max_length=15); 
	product_id = models.CharField(max_length=10); 
	product_slug = models.CharField(max_length=50); 
	product_quantity = models.CharField(max_length=5); 

# This is the place of payment
class Payment(models.Model): 
	product_id = models.CharField(max_length=10); 
	addtocart_id = models.CharField(max_length=10); 
	product_slug = models.CharField(max_length=50); 
	product_quantity = models.CharField(max_length=5); 
	payment_total_ammount = models.CharField(max_length=10); 
	payment_date = models.DateTimeField(auto_now_add=True)
	# " 'On The Way', then False " or " 'Successfully Delivered', then True "
	is_product_delivered =  models.CharField(max_length=5); 



# Create your models here.













