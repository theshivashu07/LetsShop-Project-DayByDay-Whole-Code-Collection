from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from addproducts.models import Product_Entries, OurAmazingTeam, AddToCART
# its because we want system related information, because of handling CART 
import platform




# Initial Function's to Display Pages
def index(request):
    return render(request,'index.html'); 

def aboutus(request,):
    gettingData=OurAmazingTeam.objects.all();   # to get data just dual 
    data={'gettingData' : gettingData}
    return render(request,'about-us.html',data); 

def contactus(request):
    return render(request,'contact.html'); 

def products(request):
    return render(request,'products.html'); 

def singleproduct(request,newsslug):
    myData=Product_Entries.objects.get(product_slug=newsslug);
    myStars=['1','1','1','0','']
    data={
        'myData' : myData,
        'myStars' : myStars,
    }
    return render(request,'single-product.html',data);  

def explore(request):
    return render(request,'explore.html'); 


def overallwomenarea(request):
    gettingData=getdataJustDual("Women's");   # to get data just dual 
    data={'gettingData' : gettingData}
    return render(request,'overall-products-area.html',data); 
def overallmenarea(request):
    gettingData=getdataJustDual("Men's");   # to get data just dual 
    data={'gettingData' : gettingData}
    return render(request,'overall-products-area.html',data); 
def overallkidsarea(request):
    gettingData=getdataJustDual("Kid's");   # to get data just dual 
    data={'gettingData' : gettingData}
    return render(request,'overall-products-area.html',data); 


def cartadd(request,productsslug,urllocation): 
    my_system = platform.uname()
    # Below three lines are helping us to saving duplicate data entries.....
    myData=AddToCART.objects.filter(os_name_holder=my_system.node, product_slug=productsslug);    
    if(len(myData)>0):
        return redirect(urllocation); 
    # Here we getting a slugs product id,
    myData=Product_Entries.objects.get(product_slug=productsslug);
    os_name_holder = my_system.node; 
    member_email = "";
    member_mno = "";
    product_id = myData.id;
    product_slug = productsslug;
    product_quantity = 1
    values = AddToCART( os_name_holder=os_name_holder, member_email=member_email, member_mno=member_mno, product_id=product_id, product_slug=product_slug, product_quantity=product_quantity)
    values.save();
    return redirect(urllocation); 

def cart(request):
    my_system = platform.uname()
    myData=AddToCART.objects.filter(os_name_holder=my_system.node);
    myList=[];
    totalCost=0;  # find total cost
    totalProductQuentity=0; # find all product's quentity*cast
    for data in myData:
        geteddata=Product_Entries.objects.get(id=data.product_id);
        myList.append([data,geteddata])
        print(myList[-1])
        # want to find all products 'total cost' and 'quentity*cast' below,
        totalCost=int(data.product_quantity)*int(geteddata.product_price);
        totalProductQuentity=1*int(data.product_quantity);
    alloverData={'totalCost':totalCost,'totalProduct':len(myData),'totalProductQuentity':totalProductQuentity}
    data={'gettingData':myList,'alloverData':alloverData}
    return render(request,'cart.html',data); 



def updateQuantity(request,productsslug):
    if request.method=="POST":
        print("-------------------------------------------------------")
        updatedproductquantity=request.POST["productquantity"]
        print("-------------------------------------------------------")
        values = AddToCART.objects.get(product_slug=productsslug);
        print("-------------------------------------------------------")
        values.product_quantity=updatedproductquantity;
        print("-------------------------------------------------------")
        values.save(); 
        print("-------------------------------------------------------")
        return redirect("/cart/"); 
    productData=Product_Entries.objects.get(product_slug=productsslug);
    cartedData=AddToCART.objects.get(product_slug=productsslug);
    product_name=productData.product_name
    product_quantity=cartedData.product_quantity
    product_price=productData.product_price
    product_totalprice=int(product_price)*int(product_quantity)
    product_slug=productsslug
    gettingData={'product_name':product_name, 'product_quantity':product_quantity, 'product_price':product_price, 'product_totalprice':product_totalprice, 'product_slug':product_slug}
    data={'gettingData':gettingData}
    return render(request,'updateQuantity.html',data); 

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











