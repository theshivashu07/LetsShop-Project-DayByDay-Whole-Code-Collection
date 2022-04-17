"""letsShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from letsShop import views

# these importing is must if we working with media related thing
from django.conf import settings 
from django.conf.urls.static import static 



urlpatterns = [
    # by default
    path('admin/', admin.site.urls),

    # Initial URL's for Pages
    path('',views.index,name=""),
    path('index/',views.index,name="index"),
    path('about-us/',views.aboutus,name="about-us"),
    path('contact-us/',views.contactus,name="contact-us"),
    path('products/',views.products,name="products"),
    path('single-product/<newsslug>',views.singleproduct,name="single-product"),

    path('explore/',views.explore,name="explore"), 
    path('womens/',views.overallwomenarea,name="overall-women-area"),
    path('mens/',views.overallmenarea,name="overall-men-area"),
    path('kids/',views.overallkidsarea,name="overall-kids-area"),

    path('cart/',views.cart,name="cart"), 
    path('cart-add/<slug:productsslug>/<path:urllocation>',views.cartadd,name="cart-add"), 
    # path('updatequantity/',views.updateQuantity,name="updatequantity"),
    path('updatequantity/<slug:productsslug>',views.updateQuantity,name="updatequantity"),
    path('payments/<slug:productsslug>',views.payments,name="payments"),
    #path('allpayments/<slug:productsslug>',views.allpayments,name="allpayments"),
    path('removecart/<slug:productsslug>',views.removeCart,name="removecart"),
    # actually here wa want to take cart id, so that according to this we remove this product order
    path('canceledthisorder/<int:addtocart>',views.canceledThisOrder,name="canceledthisorder"),
] 



# this is also must if we working with media related things
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)







"""

Way-1 : Here we use our first way, by urls
| overall-products-area.html
    <li><a type="submit" href="/cart-add/{{data.product_slug}}/{{request.path}}"><i class="fa fa-shopping-cart"></i></a></li>
| urls.py
    path('cart-add/<slug:productsslug>/<path:urllocation>',views.cartadd,name="cart-add"), 
| views.py
def cartadd(request,productsslug,urllocation): 
    ...................
    return redirect(urllocation); 

Way-2 : Here we use our first way, by urls fuctions
| overall-products-area.html
    <li><a type="submit" href="{% url 'cart-add' urllocation=request.path productsslug=data.product_slug %}"><i class="fa fa-shopping-cart"></i></a></li>
| urls.py
    path('cart-add/<slug:productsslug>/<path:urllocation>',views.cartadd,name="cart-add"), 
| views.py
def cartadd(request,productsslug,urllocation): 


"""


'''
    # trial if you wants any value pass on url,
    # so there is two ways, set its type, or everytype also.
    path('products/<productsid>',views.productsDetails),
    path('products/<int:productsid>',views.productsDetails),
''' 
