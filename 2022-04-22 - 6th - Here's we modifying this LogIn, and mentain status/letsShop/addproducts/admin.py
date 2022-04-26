from django.contrib import admin
from addproducts.models import Product_Entries, OurAmazingTeam, AddToCART, Payment, SignIn, LogIn

class saveProductEntries(admin.ModelAdmin):
	list_display=('product_from', 'product_name', 'product_price', 'product_create_date', 'product_update_date','product_image');
admin.site.register(Product_Entries,saveProductEntries);

class saveOurAmazingTeam(admin.ModelAdmin):
	list_display=('member_name', 'member_role', 'member_instagram_id', 'member_facebook_id', 'member_twitter_id','member_linkedin_id','member_github_id');
admin.site.register(OurAmazingTeam,saveOurAmazingTeam);

class saveAddToCART(admin.ModelAdmin): 
	list_display=('os_name_holder', 'member_email', 'member_mno', 'product_slug', 'product_quantity', 'is_payment_done', 'is_product_delivered'); 
admin.site.register(AddToCART,saveAddToCART); 

class savePayment(admin.ModelAdmin): 
	list_display=( 'product_slug', 'product_quantity', 'payment_total_ammount', 'payment_date', 'is_product_delivered' ); 
admin.site.register(Payment,savePayment); 

class saveSignIn(admin.ModelAdmin):
	list_display=('os_name_holder', 'client_username', 'client_name', 'client_email', 'client_mno', 'client_address','client_areapincode','client_signin_date');
admin.site.register(SignIn,saveSignIn);

class saveLogIn(admin.ModelAdmin):
	list_display=('os_name_holder', 'client_name', 'client_loginby', 'client_username', 'client_login_date', 'client_status');
admin.site.register(LogIn,saveLogIn);









"""
# Alternative of above,
admin.site.register(Product_Entries); 
admin.site.register(OurAmazingTeam); 
admin.site.register(AddToCART); 
admin.site.register(Payment); 
admin.site.register(SignIn); 
admin.site.register(LogIn); 
"""



# Register your models here.






