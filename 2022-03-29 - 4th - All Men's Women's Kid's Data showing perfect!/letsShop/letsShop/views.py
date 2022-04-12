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
    gettingData=getdataJustDual("Women's");   # to get data just dual 
    data={'gettingData' : gettingData}
    return render(request,'overall-women-area.html',data); 

def overallmenarea(request):
    gettingData=getdataJustDual("Men's");   # to get data just dual 
    data={'gettingData' : gettingData}
    return render(request,'overall-men-area.html',data); 

def overallkidsarea(request):
    gettingData=getdataJustDual("Kid's");   # to get data just dual 
    data={'gettingData' : gettingData}
    return render(request,'overall-kids-area.html',data); 


# One extra function, suppose we have data but we want to dual it
# Actually we have only three products, but we want to show as 6, that why it needed,
def getdataJustDual(bases):
    myData=Product_Entries.objects.filter(product_from=bases);    # to get all data from database
    gettingData = []
    for data in myData:
        gettingData.append(data)
    for data in myData:
        gettingData.append(data)
    return gettingData;







# To check initially, how "HttpResponse" works.
'''
def index(request):
        return HttpResponse("<b>Okay Google!</b>")
'''


