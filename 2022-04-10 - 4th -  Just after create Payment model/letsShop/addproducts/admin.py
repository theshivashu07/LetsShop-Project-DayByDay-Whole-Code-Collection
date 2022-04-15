from django.contrib import admin
from addproducts.models import Product_Entries, OurAmazingTeam, AddToCART, Payment

class saveProductEntries(admin.ModelAdmin):
	list_display=('product_from', 'product_name', 'product_price', 'product_create_date', 'product_update_date','product_image');
admin.site.register(Product_Entries,saveProductEntries);

class saveOurAmazingTeam(admin.ModelAdmin):
	list_display=('member_name', 'member_role', 'member_instagram_id', 'member_facebook_id', 'member_twitter_id','member_linkedin_id','member_github_id');
admin.site.register(OurAmazingTeam,saveOurAmazingTeam);

class saveAddToCART(admin.ModelAdmin): 
	list_display=('os_name_holder', 'member_email', 'member_mno', 'product_id', 'product_slug', 'product_quantity'); 
admin.site.register(AddToCART,saveAddToCART); 

class savePayment(admin.ModelAdmin): 
	list_display=('product_id', 'is_product_delivered', 'product_slug', 'product_quantity', 'payment_total_ammount', 'payment_date'); 
admin.site.register(Payment,savePayment); 


# Register your models here.






