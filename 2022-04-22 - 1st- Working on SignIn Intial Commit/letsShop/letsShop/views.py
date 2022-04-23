from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from addproducts.models import Product_Entries, OurAmazingTeam, AddToCART, Payment, SignIn, LogIn
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


def canceledThisOrder(request,addtocart): 
    # below code is if you want to cancel order, and also remove on cart...
    cartedData=AddToCART.objects.get(id=addtocart); 
    paymentData=Payment.objects.get(addtocart_id=addtocart); 
    cartedData.delete(); 
    paymentData.delete(); 
    return redirect("/cart/"); 
    '''
    # below code is if you want to cancel order, but not remove on cart...
    cartedData=AddToCART.objects.get(id=addtocart); 
    cartedData.is_payment_done="No"
    cartedData.save()
    paymentData=Payment.objects.get(addtocart_id=addtocart);
    paymentData.delete(); 
    return redirect("/cart/"); 
    '''






#####################################################################################
#####################################################################################

def usersSignIn(request,passes): 
    print(f"You are on '{passes}' url");
    if request.method=="POST":

        if(passes=="generateotp"):
            my_system = platform.uname()
            myOTP=myPassword()
            print(f"Your OTP is : <{myOTP}>")
            values = SignIn( 
                os_name_holder=my_system.node, 
                client_name=request.POST["name"],
                client_email=request.POST["email"],
                client_mno=request.POST["mno"],
                client_address=request.POST["address"],
                client_areapincode=request.POST["areapincode"],
                client_varificationby=request.POST["varifyby"],
                client_five_varification_codes=None,
                client_last_otp=myOTP,
            ) 
            values.save();
            data={
                'hiddenkey' : '1',
                'passdata':"otpchecking",
                'signin' : values,
            }
            return render(request,'userssignin.html',data); 

        # here we check OTP is write or not, if write then moving it get username and password...
        elif(passes=="otpchecking"): 
            my_system = platform.uname()
            getedOTP=request.POST["getedOTP"];
            allValues = SignIn.objects.filter(os_name_holder=my_system.node); 
            values=allValues[len(allValues)-1]
            # this section is because if our OTP is wrong  
            if(values.client_last_otp!=getedOTP):
                return redirect("/userssignin/wrongotp"); 
            # this section is because if our OTP is correct
            data={
                'hiddenkey' : '2',
                'passdata':"getusernamepassword",
                'signin' : values,
            }
            return render(request,'userssignin.html',data);

        # here all password checkings
        elif(passes=="getusernamepassword"): 
            # dont storevalues saperated with coma, otherwise data store in tuple format, like:(vashu,).
            client_username=request.POST["username"];
            client_password=request.POST["password"];
            client_confirm_password=request.POST["confirmpassword"];
            if(client_password!=client_confirm_password):
                return redirect("/userssignin/ifpasswordnotmatch"); 
            my_system = platform.uname()
            allValues = SignIn.objects.filter(os_name_holder=my_system.node); 
            values=allValues[len(allValues)-1]
            values.client_username=client_username
            values.client_password=client_password
            values.client_last_otp="NILL"
            values.save()
            return redirect("/userslogin/"); 

    # this section is because if our OTP is wrong 
    if(passes=="wrongotp"):
        my_system = platform.uname()
        allValues = SignIn.objects.filter(os_name_holder=my_system.node); 
        values=allValues[len(allValues)-1]
        myOTP=myPassword()
        print(f"Your New OTP is : <{myOTP}>")
        values.client_last_otp=myOTP;
        values.save();
        data={
            'hiddenkey' : '1',
            'passdata':"otpchecking", 
            'signin' : values,
        }
        return render(request,'userssignin.html',data);

    # if we put a wrong mismatch passwords
    if(passes=="ifpasswordnotmatch"): 
        my_system = platform.uname()
        allValues = SignIn.objects.filter(os_name_holder=my_system.node); 
        values=allValues[len(allValues)-1]
        data={
            'hiddenkey' : '2',
            'passdata':"getusernamepassword",
            'signin' : values,
        }
        return render(request,'userssignin.html',data);

    # Its a bydefault section, if urls passing string is not matching then bydefault considering this...
    # a function to delete all data tables, where we not assign OTP and username and password
    # and this function runs only whenever we initially running this sign in option...
    allValues = SignIn.objects.filter(client_username=""); 
    for i in allValues:
        i.delete()
    data={
        'hiddenkey':'0',
        'passdata':"generateotp",
    }
    return render(request,'userssignin.html',data); 


#####################################################################################
#####################################################################################

def usersLogIn(request): 
    data={}; 
    return render(request,'userslogin.html',data); 

#####################################################################################
#####################################################################################














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



def myPassword():
        # Refrence link : https://www.geeksforgeeks.org/generating-strong-password-using-python/
        import random
        import array
        MAX_LEN = 12
        DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
        LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                             'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                             'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<']
        # combines all the character arrays above to form one array
        COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS
        # randomly select at least one character from each character set above
        rand_digit = random.choice(DIGITS)
        rand_upper = random.choice(UPCASE_CHARACTERS)
        rand_lower = random.choice(LOCASE_CHARACTERS)
        rand_symbol = random.choice(SYMBOLS)
        temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol
        for x in range(MAX_LEN - 4):
            temp_pass = temp_pass + random.choice(COMBINED_LIST)
        temp_pass_list = array.array('u', temp_pass)
        random.shuffle(temp_pass_list)

        password = ""
        for x in temp_pass_list:
                password = password + x;
        return password;











