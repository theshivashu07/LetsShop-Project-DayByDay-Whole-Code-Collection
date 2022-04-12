from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from addproducts.models import Product_Entries



# Initial Function's to Display Pages
def index(request):
    return render(request,'index.html'); 
def aboutus(request):
    return render(request,'about-us.html'); 
def contactus(request):
    return render(request,'contact.html'); 
def products(request):
    return render(request,'products.html'); 
def singleproduct(request):
    return render(request,'single-product.html'); 

def explore(request):
    return render(request,'explore.html'); 
def overallwomenarea(request):
    return render(request,'overall-women-area.html'); 
def overallmenarea(request):
    data={}
    gettingData=Product_Entries.objects.all();    # to get all data from database
    gettingData=getdataJustDual(gettingData);   # to get data just dual 
    data={'gettingData' : gettingData}
    return render(request,'overall-men-area.html',data); 
def overallkidsarea(request):
    return render(request,'overall-kids-area.html'); 


# One extra function, suppose we have data but we want to dual it
def getdataJustDual(myData):
    gettingData = []
    for data in myData:
        gettingData.append(data)
        print(data.product_image)
    for data in myData:
        gettingData.append(data)
        print(data.product_image)
    return gettingData;




'''
def aboutus(request):
    return render(request,'newsdetails.html',data); 
def course(request):
    return render(request,'newsdetails.html',data); 
'''

# To check initially, how "HttpResponse" works.
'''
def index(request):
        return HttpResponse("<b>Okay Google!</b>")
'''


