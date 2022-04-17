from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from addproducts.models import Product_Entries, OurAmazingTeam, AddToCART, Payment
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
    # Below lines we are protecting to save data re-entry, if last's payment done then skipp, otherwise incress quentity,
    myData=AddToCART.objects.filter(os_name_holder=my_system.node, product_slug=productsslug, is_payment_done="No");    
    # myData=myData[len(myData)-1];  # its because we want to check only lasts
    if(len(myData)>0): 
        return redirect('/updatequantity/'+myData[0].product_slug)
    # Here we getting a slugs product id,
    myData=Product_Entries.objects.get(product_slug=productsslug);
    values = AddToCART( 
        os_name_holder=my_system.node, 
        member_email="", 
        member_mno="", 
        product_id=myData.id, 
        product_slug=productsslug, 
        product_quantity=1,
        is_payment_done="No",
        is_product_delivered="No",
    ) 
    values.save();
    return redirect(urllocation); 

def cart(request):
    my_system = platform.uname()
    # below one line is vyvastha, suppose we product divered then not need that product show on 'cart'
    myData=AddToCART.objects.filter(os_name_holder=my_system.node, is_product_delivered="No");
    myList=[];
    # find 'total cost' __and__ find all 'product's quentity*cast' __and__ 'total product'
    totalCost,totalProductQuentity,totalProduct=0,0,0; 
    for data in myData:
        getedproductdata = Product_Entries.objects.get(id=data.product_id);
        myList.append([data,getedproductdata])
        # condition is if our payment is already done then why we count this mony,
        # actually we want to add carts which payments done, but not count on "alloverData"
        if(data.is_payment_done=="Yes"):
            continue;
        # want to find 'total cost' __and__ find all 'product's quentity*cast' __and__ 'total product'
        totalProduct = totalProduct + 1;
        totalCost = (int(data.product_quantity)*int(getedproductdata.product_price)) + totalCost; 
        totalProductQuentity = (1*int(data.product_quantity)) + totalProductQuentity;
    data={
        'gettingData':myList,
        'alloverData':{ 
            'totalCost':totalCost, 
            'totalProduct':totalProduct, 
            'totalProductQuentity':totalProductQuentity, 
        }
    }
    return render(request,'cart.html',data); 


# here we update our quentity by post method
def updateQuantity(request,productsslug):
    if request.method=="POST":
        updatedproductquantity=request.POST["productquantity"]
        values = AddToCART.objects.get(product_slug=productsslug, is_payment_done="No");
        values.product_quantity=updatedproductquantity;
        values.save(); 
        return redirect("/cart/"); 
    productData=Product_Entries.objects.get(product_slug=productsslug);
    cartedData=AddToCART.objects.get(product_slug=productsslug, is_payment_done="No");
    gettingData={
        'product_name' : productData.product_name, 
        'product_quantity' : cartedData.product_quantity, 
        'product_price' : productData.product_price, 
        'product_totalprice' : int(cartedData.product_quantity) * int(productData.product_price),  
        'product_slug' : productsslug
    }
    data={'gettingData' : gettingData}
    return render(request,'updateQuantity.html',data); 


def payments(request,productsslug): 
    def myFunc(productsslug):
        productData=Product_Entries.objects.get(product_slug=productsslug);
        cartedData=AddToCART.objects.get(product_slug=productsslug, is_payment_done="No");
        cartedData.is_payment_done="Yes"
        cartedData.save()
        # paymentData=Payment.objects.get(product_slug=productsslug);
        values = Payment( 
            product_id = productData.id, 
            addtocart_id = cartedData.id, 
            product_slug = productsslug, 
            product_quantity = cartedData.product_quantity, 
            payment_total_ammount = int(cartedData.product_quantity) * int(productData.product_price), 
            is_product_delivered = "No"
        )
        values.save();
    # All the this function's real working code is there.....
    if(productsslug=="all-payments"):
        my_system = platform.uname()
        myData=AddToCART.objects.filter(os_name_holder=my_system.node, is_payment_done="No");
        for data in myData:
            myFunc(data.product_slug)
        return redirect("/cart/"); 
    myFunc(productsslug)
    return redirect("/cart/"); 


def removeCart(request,productsslug): 
    cartedData=AddToCART.objects.get(product_slug=productsslug, is_payment_done="No"); 
    cartedData.delete(); 
    return redirect("/cart/"); 




        




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











