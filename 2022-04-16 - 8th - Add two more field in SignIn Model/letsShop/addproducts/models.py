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
	def __str__(self):
		return f"We adding \"{self.product_name}\" product, for \"{self.product_from}\". Price : {self.product_price}/-";

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
	def __str__(self):
		return  f"\"{self.member_name}\" has joined our team, as a \"{self.member_role}\"";

# Here we manage all cart related data
class AddToCART(models.Model): 
	os_name_holder = models.CharField(max_length=50); 
	member_email = models.CharField(max_length=70, null=True, blank=True); 
	member_mno = models.CharField(max_length=15, null=True, blank=True); 
	product_id = models.CharField(max_length=10); 
	product_slug = models.CharField(max_length=50); 
	product_quantity = models.CharField(max_length=5); 
	# Under Both of then, 'No' then False,  and 'Yes' then True 
	is_payment_done =  models.CharField(max_length=5, null=True, blank=True); 
	is_product_delivered =  models.CharField(max_length=5, null=True, blank=True); 
	def __str__(self):
		return  f"{self.product_slug}'s {self.product_quantity} product's Added on CART!"

# This is the place of payment
class Payment(models.Model): 
	product_id = models.CharField(max_length=10); 
	addtocart_id = models.CharField(max_length=10); 
	product_slug = models.CharField(max_length=50); 
	product_quantity = models.CharField(max_length=5); 
	payment_total_ammount = models.CharField(max_length=10); 
	payment_date = models.DateTimeField(auto_now_add=True)
	is_product_delivered =  models.CharField(max_length=5); 
	def __str__(self):
		return f"{self.product_slug}'s {self.product_quantity} product's payment is DONE!";

# This is a SignIn model
class SignIn(models.Model): 
	os_name_holder = models.CharField(max_length=50); 
	client_name = models.CharField(max_length=50); 
	client_email = models.CharField(max_length=35); 
	client_mno = models.CharField(max_length=15); 
	client_address = models.CharField(max_length=100); 
	client_areapincode = models.CharField(max_length=10); 
	client_signin_date = models.DateTimeField(auto_now_add=True)
	client_username =  models.CharField(max_length=35); 
	client_password =  models.CharField(max_length=35); 
	client_varificationby = models.CharField(max_length=35, null=True, blank=True); 
	client_five_varification_codes = models.CharField(max_length=30, null=True, blank=True); 
	def __str__(self):
		return f"{self.client_name} is SignIn Now! as @{self.client_username}.";

# This is a LogIn model
class LogIn(models.Model): 
	os_name_holder = models.CharField(max_length=50); 
	client_id = models.CharField(max_length=10); 
	client_name = models.CharField(max_length=50); 
	client_loginby = models.CharField(max_length=35); 
	client_username =  models.CharField(max_length=35); 
	client_password =  models.CharField(max_length=35); 
	client_login_date = models.DateTimeField(auto_now=True);
	# If login then 'True', and if logout then 'False' status is show
	client_status =  models.CharField(max_length=10); 
	def __str__(self):
		return f"{self.client_name} is Active Now! as @{self.client_username}."; 



# Create your models here.















