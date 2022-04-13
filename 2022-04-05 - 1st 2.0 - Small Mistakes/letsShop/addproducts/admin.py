from django.contrib import admin
from addproducts.models import Product_Entries, OurAmazingTeam

class saveProductEntries(admin.ModelAdmin):
	list_display=('product_from', 'product_name', 'product_price', 'product_create_date', 'product_update_date','product_image');
admin.site.register(Product_Entries,saveProductEntries);

class saveOurAmazingTeam(admin.ModelAdmin):
	list_display=('member_name', 'member_role', 'member_instagram_id', 'member_facebook_id', 'member_twitter_id','member_linkedin_id','member_github_id');
admin.site.register(OurAmazingTeam,saveOurAmazingTeam);

# Register your models here.









