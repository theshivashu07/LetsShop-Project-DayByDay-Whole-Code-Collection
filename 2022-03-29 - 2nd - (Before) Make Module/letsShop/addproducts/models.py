from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField

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





	"""

	# this is also one of the best consept, but we implementing this in the future...
	def __str__(self):
		return self.my_name+" is Inserted details.";
		

	# And this logic is not working to create a saperate wise according to product_from, may be its logic is somethig else,
	# by the way its logic is coming from, when we do these thing from front-end, so there we set that, upcoming data goes, 
	# directly "products/"+"mens/"+"mypick.jpg",
	product_image = models.FileField(upload_to="products/"+str(product_from)+"/", max_length=250,null=True,default=None);

	"""














# Create your models here.
