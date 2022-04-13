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

class AddToCART(models.Model): 
	os_name_holder =  models.CharField(max_length=50); 
	member_email =  models.CharField(max_length=70); 
	member_mno =  models.CharField(max_length=15); 
	product_id = models.CharField(max_length=10); 
	product_slug = models.CharField(max_length=50); 



# Create your models here.











	"""

	# this is also one of the best consept, but we implementing this in the future...
	def __str__(self):
		return self.my_name+" is Inserted details.";
		

class Product_Entries(models.Model):
	product_from = models.CharField(max_length=50);
	product_name = models.CharField(max_length=100);
	product_details = HTMLField(); 
	product_price = models.CharField(max_length=10);
	# we adding this field because we want to add image's too.
	product_image = models.FileField(upload_to="products/", max_length=250,null=True,default=None);
	# we also make internal slug's on the bases of my_name, may be in future we needed these! 
	product_slug = AutoSlugField(populate_from='product_name', unique=True, null=True, default=None);
	# we don't want to update our date every time, so we use this
	product_create_date = models.DateTimeField(auto_now_add=True)
	# but we want to track our last updation, to it help to track last
	product_update_date = models.DateTimeField(auto_now=True)

	# we want to show this field as hidden, and its must field, 
	# but now i dont know that how we manage this?!!
	# product_stars = models.CharField(max_length=1);

	# And this logic is not working to create a saperate wise according to product_from, may be its logic is somethig else,
	# by the way its logic is coming from, when we do these thing from front-end, so there we set that, upcoming data goes, 
	# directly "products/"+"mens/"+"mypick.jpg",
	# product_image = models.FileField(upload_to="products/"+str(product_from)+"/", max_length=250,null=True,default=None);





class OurAmazingTeam(models.Model):
	member_name =  models.CharField(max_length=50);
	member_role =  models.CharField(max_length=50, null=True, blank=True);
	member_email_id = models.EmailField(max_length = 100, null=True, blank=True, unique=True)
	member_mobilenumber = models.CharField(max_length=15, null=True, blank=True, unique=True);
	member_image = models.FileField(upload_to="products/", max_length=250,default=None,blank=True,null=True); 
	member_about_section = HTMLField(null=True, blank=True); 
	member_username = models.CharField(max_length=50, unique=True); 
	member_password = models.CharField(max_length=50);
	member_age = models.CharField(max_length=3, null=True, blank=True);
	member_instagram_id = models.CharField(max_length=100, null=True, blank=True, unique=True);
	member_facebook_id = models.CharField(max_length=100, null=True, blank=True, unique=True);
	member_twitter_id = models.CharField(max_length=100, null=True, blank=True, unique=True);
	member_linkedin_id = models.CharField(max_length=100, null=True, blank=True, unique=True);
	member_github_id = models.CharField(max_length=100, null=True, blank=True, unique=True); 
	member_slug = AutoSlugField(populate_from='member_name', unique=True, null=True, default=None);
	# "null=True" is not working for FileField and HTMLField,
	# But still "blank=True" is working, which means data insertion is not must,
	# if we not write anything about "blank" attribute, or write "blank=False", which means insertion is not must.



	"""











