from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect


# To check initially, how "HttpResponse" works.
'''
def index(request):
        return HttpResponse("<b>Okay Google!</b>")
'''


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
    return render(request,'overall-men-area.html'); 
def overallkidsarea(request):
    return render(request,'overall-kids-area.html'); 



'''
def aboutus(request):
    return render(request,'newsdetails.html',data); 
def course(request):
    return render(request,'newsdetails.html',data); 
'''



