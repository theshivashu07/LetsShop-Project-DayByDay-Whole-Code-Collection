from django.contrib import admin
from addproducts.models import Product_Entries

class saveProductEntries(admin.ModelAdmin):
	list_display=('product_from', 'product_name', 'product_price', 'product_create_date', 'product_update_date','product_image');
admin.site.register(Product_Entries,saveProductEntries);


# Register your models here.










