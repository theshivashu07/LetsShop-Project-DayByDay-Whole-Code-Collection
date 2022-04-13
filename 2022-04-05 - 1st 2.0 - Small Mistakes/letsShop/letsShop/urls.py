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

    # path('contact/',views.contact,name="contact"),
]





# this is also must if we working with media related things
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)







'''
    # trial if you wants any value pass on url,
    # so there is two ways, set its type, or everytype also.
    path('products/<productsid>',views.productsDetails),
    path('products/<int:productsid>',views.productsDetails),
''' 
