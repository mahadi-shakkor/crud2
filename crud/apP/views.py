from django.shortcuts import render
from .models import *
from .forms import *
from django.shortcuts import render

from django.shortcuts import render, get_object_or_404

import datetime

def add_harvest_info(request):
    userid = request.GET.get('userid')
    products = Product.objects.all() 
    
    try:
        user = User.objects.get(userid=userid)
    except User.DoesNotExist:
        # Handle the case where the user doesn't exist (optional)
        user = None
    if request.method == 'POST':
        product_id = request.POST.get('product')
        product = get_object_or_404(Product, product_id=product_id)
        print(product.product_name)


        pass

    
    return render(request, 'add_harvest_info.html',{"user":user,"product":products})



def PDemandf(request):

    
    userid = request.GET.get('userid')  
    user = get_object_or_404(User, userid=userid)  
    products = Product.objects.all()  


    for i in products:
        print(i.product_name)
    if request.method == 'POST':
        location = LocationForm(request.POST)
        if location.is_valid() :  # Check both forms' validity
            location_instance = location.save(commit=False)
            # Print to check values
            print(location_instance.city, location_instance.state)
            location_instance.save()
            print("valid loation")
        

        print("user __>>"+user.name)

        print("in post end ")  

                # Get the selected value from the radio button group
        selected_option = request.POST.get('flexRadioDefault')
        comments = request.POST.get('comments')

        product_id = request.POST.get('product_id')
        demandamount = request.POST.get('demandamount')

        demand_date_time = request.POST.get('demand_date_time')
        state = request.POST.get('state')
        season = request.POST.get('season')
        area = request.POST.get('area')
        price_should_be = request.POST.get('price_should_be')




        product = get_object_or_404(Product, product_id=product_id)


        print("---------------------------------------------------------------------------------------------------------------")
        # Print the values in a structured and readable format
        print(f"Selected Option: {selected_option}")
        print(f"Product ID: {product_id}")
        print(f"Demand Amount: {demandamount}")
        print(f"Demand Date and Time: {demand_date_time}")
        print(f"State: {state}")
        print(f"area: {area}")
        print(f"Season: {season}")


        print("---------------------------------------------------------------------------------------------------------------")



        # # Check which option was selected
        # if selected_option == "KG":
        #     message = "You selected KG"
        # elif selected_option == "TON":
        #     message = "You selected TON."
        # elif selected_option == "MON":
        #     message = "You selected MON."
        # else:
        #     message = "No valid option selected."
        # print(message)

        l = PDemand.objects.create(mon=(selected_option=="MON"),kg=(selected_option=="KG"),ton=(selected_option=="TON"),price_should_be=price_should_be,demandamount=demandamount,demand_date_time=demand_date_time,comments=comments,season=season,area=area,state=state,product_id=product_id,locationid=location_instance,userid=user,)

        # location.save()
               
       

        


        
        

    else:
        
        location = LocationForm()

    
       

    return render(request, 'PDemand.html', {"products":products,"user": user, 'location': location})






def monitir_realtime_tem_humidity(request):
    userid = request.GET.get('userid')
    
    try:
        user = User.objects.get(userid=userid)
    except User.DoesNotExist:
        # Handle the case where the user doesn't exist (optional)
        user = None
    
    # Get all batches where the user matches
    batch = Batch.objects.filter(user=user).order_by('-date_time_batch_created')
    # batch=Batch.objects.all()
    
    return render(request, 'monitir_realtime_tem_humidity.html', {'batch': batch})



    # return render(request, 'monitir_realtime_tem_humidity.html')

def add_batch_to_invantory(request):
    text='';

    userid = request.GET.get('userid')
    user = User.objects.get(userid=userid)
    location1=user.location
    product=Product.objects.all()







    # print()
    
    if request.method == "POST":
        
        # Collect data from the POST request
        product_id = request.POST.get("product")
        sell = request.POST.get("sell")
        stor = request.POST.get("stor")
        temperature = request.POST.get("temperature")
        humidity = request.POST.get("humidity")
        batch_count = request.POST.get("c")
        datetime_value = request.POST.get("datetime")
        unit = request.POST.get("u")
        per_unit_price = request.POST.get("float_value")
        description = request.POST.get("description")
        product_amount = request.POST.get("product_amount")
        street = request.POST.get("street")
        city = request.POST.get("city")
        state = request.POST.get("state")
        country = request.POST.get("country")
        latitude = request.POST.get("latitude")
        longitude = request.POST.get("longitude")
        altitude = request.POST.get("altitude")
        timezone = request.POST.get("timezone")
        Set_my_L_batch_L = request.POST.get("Set_my_L_batch_L")
        KG=0
        TON=0
        MON=0
        if (unit=="KG"):
            KG=1
        elif(unit=="TON"):
            TON=1
        else:
            MON=1       

        if (sell):
            sell=1
        else:
            sell=0
        if (stor):
            stor=1
        else:
            stor=0    


        # if(Set_my_L_batch_L):
        #     print("chacked")
        # else:
        #     print("not chacked")    
        if altitude=='':
            altitude=10
        # print(product_id)   
        p1 = Product.objects.get(product_id=product_id) 
        # print(p1.product_id)
        # print("Form data received:")
        # print(f"Product ID: {product_id}")
        # print(f"Sell: {sell}")
        # print(f"Store: {stor}")
        # print(f"Temperature: {temperature}")
        # print(f"Humidity: {humidity}")
        # print(f"Batch count: {batch_count}")
        # print(f"DateTime: {datetime_value}")
        # print(f"Unit: {unit}")
        # print(f"Per unit price: {per_unit_price}")
        # print(f"Description: {description}")
        # print(f"Product amount per batch: {product_amount}")
        # print(f"Location: {street}, {city}, {state}, {country}")
        # print(f"Latitude: {latitude}")
        # print(f"Longitude: {longitude}")
        # print(f"Altitude: {altitude}")
        # print(f"Timezone: {timezone}")

        
        
        if(Set_my_L_batch_L):           
            location=location1
            
        else:

            location = Location.objects.create(
                latitude=latitude,
                longitude=longitude,
                altitude=altitude,
                timezone=timezone,
                street=street,
                city=city,
                state=state,
                country=country      
                  )
            

        for i in range(int(batch_count)):
            Batch.objects.create(
                product=p1,
                user=user,
                location=location,                
                product_amount=product_amount,  # Product Amount
                sell=sell,  # SELL as True (1)
                store=stor,  # STORE as True (1)
                optimum_temperature_to_store=temperature,  # Optimum Temperature
                optimum_humidity_to_store=humidity,  # Optimum Humidity
                product_unit_price=per_unit_price,  # Product Unit Price
                kg=KG,  # Example Unit for KG (can be None or another unit if needed)
                ton=TON,  # Example Unit for TON (can be None or another unit if needed)
                mon=MON,  # Example Unit for MON (can be None or another unit if needed)
                batch_description=description,  # Description of the batch
                date_time_batch_created=datetime.now(),  # Current datetime
            )

        
        

        




        return render(request, 'add_batch_to_invantory.html', {"text": "text","product":product,"location":location1})



    return render(request, 'add_batch_to_invantory.html', {"text": "New batch added","product":product,"location":location1})
# # --------------------------------------------------====================================================





#     userid = request.GET.get('userid')
    
#     try:
#         user = User.objects.get(userid=userid)
#         location=user.location
#         product=Product.objects.all()
#     except:
#         return HttpResponse("user not found")
#     if request.method == "POST":
#         # Collect data from the POST request
#         product_id = request.POST.get("product")
#         sell = request.POST.get("sell")
#         stor = request.POST.get("stor")
#         temperature = request.POST.get("temperature")
#         humidity = request.POST.get("humidity")
#         batch_count = request.POST.get("c")
#         datetime_value = request.POST.get("datetime")
#         unit = request.POST.get("u")
#         per_unit_price = request.POST.get("float_value")
#         description = request.POST.get("description")
#         product_amount = request.POST.get("product_amount")
#         street = request.POST.get("street")
#         city = request.POST.get("city")
#         state = request.POST.get("state")
#         country = request.POST.get("country")
#         latitude = request.POST.get("latitude")
#         longitude = request.POST.get("longitude")
#         altitude = request.POST.get("altitude")
#         timezone = request.POST.get("timezone")
#         print("Form data received:")
#         print(f"Product ID: {product_id}")
#         print(f"Sell: {sell}")
#         print(f"Store: {stor}")
#         print(f"Temperature: {temperature}")
#         print(f"Humidity: {humidity}")
#         print(f"Batch count: {batch_count}")
#         print(f"DateTime: {datetime_value}")
#         print(f"Unit: {unit}")
#         print(f"Per unit price: {per_unit_price}")
#         print(f"Description: {description}")
#         print(f"Product amount per batch: {product_amount}")
#         print(f"Location: {street}, {city}, {state}, {country}")
#         print(f"Latitude: {latitude}")
#         print(f"Longitude: {longitude}")
#         print(f"Altitude: {altitude}")
#         print(f"Timezone: {timezone}")

#         # try:
#         #     location = Location.objects.create(
#         #         latitude=latitude,
#         #         longitude=longitude,
#         #         altitude=altitude,
#         #         timezone=timezone,
#         #         street=street,
#         #         city=city,
#         #         state=state,
#         #         country=country

               
#         #     )
#         #     product = Product.objects.get(product_id=int(product_id))
            
#         #     # Assuming you have valid Location, Product, User, and Harvest objects with corresponding IDs.
#         #     location = Location.objects.get(id=1)  # Replace with valid Location ID
#         #     product = Product.objects.get(id=10)  # Replace with valid Product ID
#         #     user = User.objects.get(id=1)  # Replace with valid User ID
#         #     # harvest = Harvest.objects.get(id=1)  # Replace with valid Harvest ID

#         #     # Create a new Batch entry


            

            
#         # except Exception as e:
#         #     # If there is an error with saving the location, return an error message
#         #     return render(request, 'add_batch_to_invantory.html', {"text": f"Error saving location: {str(e)}","user":user,"location":location,"product":product})

#         return render(request, 'add_batch_to_invantory.html', {"text": "batch added successfully!","user":user,"location":location,"product":product})






#     return render(request,"add_batch_to_invantory.html",{"user":user,"location":location,"product":product})

from datetime import datetime
def dashboard2(request):
    return render(request,"dashboard2.html")

def signup2(request):
    if request.method == 'POST':
        # Retrieve user input from the form
        user_id = request.POST.get('id')
        password = request.POST.get('password')

        # Simple validation: Check if user exists
        try:
            user = User.objects.get(userid=user_id)  # Assuming `id` is either email or user ID
            if user.password == password:
                # If password matches, return success message
                return render(request, 'dashboard2.html', {"text": "Login successful!","user":user})
            else:
                # If password does not match, show an error message
                return render(request, 'signup2.html', {"text": "Incorrect password!"})
        except User.DoesNotExist:
            # If the user does not exist, show an error message
            return render(request, 'signup2.html', {"text": "User not found!"})

    # If the form is not submitted, just render the form page
    return render(request, 'signup2.html')



def user_signup_form(request):
    if request.method == 'POST':
        # Get the user registration data from the form
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        usercontactnumber = request.POST.get('usercontactnumber')
        usertype = request.POST.get('usertype')
        street = request.POST.get('street')
        city = request.POST.get('city')
        state = request.POST.get('state')
        country = request.POST.get('country')

        # Get the location data from the form
        latitude = request.POST.get('latitude')  
        longitude = request.POST.get('longitude')
        altitude = request.POST.get('altitude')
        timezone = request.POST.get('timezone')

        # Initialize an empty error message list
        errors = []

        # Validation checks
        if not name:
            errors.append("Name is required.")
        if not email:
            errors.append("Email is required.")
        elif '@' not in email:
            errors.append("Invalid email format.")
        if not password or len(password) < 6:
            errors.append("Password is required and must be at least 6 characters long.")
        if not usercontactnumber or len(usercontactnumber) < 10:
            errors.append("Contact number is required and must be at least 10 digits.")
        if not street:
            errors.append("Street address is required.")
        if not city:
            errors.append("City is required.")
        if not state:
            errors.append("State is required.")
        if not country:
            errors.append("Country is required.")
        if not latitude or not longitude:
            errors.append("Location (latitude and longitude) is required.")

        # If there are errors, return the form with error messages
        if errors:
            return render(request, 'user_signup_form.html', {"text": " ".join(errors)})
        
        # Create Location object and save it to the database
        try:
            location = Location.objects.create(
                latitude=latitude,
                longitude=longitude,
                altitude=altitude,
                timezone=timezone,
                street=street,
                city=city,
                state=state,
                country=country
            )
            
        except Exception as e:
            # If there is an error with saving the location, return an error message
            return render(request, 'user_signup_form.html', {"text": f"Error saving location: {str(e)}"})

        # Create User object and save it to the database
        try:
            user = User.objects.create(
                name=name,
                email=email,
                password=password,
                usercontactnumber=usercontactnumber,
                usertype=usertype,
                location=location  # Associate the user with the created location
            )





            if user.usertype == "nutritionist":
                Nutritionists.objects.create(nid=user)  # Create a Nutritionist instance linked to the user
            elif user.usertype == "warehouse_manager":
                WirehouseManager.objects.create(wid=user)  # Create a WarehouseManager instance linked to the user
            elif user.usertype == "retailer":
                Retailer.objects.create(rid=user)  # Create a Retailer instance linked to the user
            elif user.usertype == "farmer":
                Farmer.objects.create(fid=user)  # Create a Farmer instance linked to the user
            elif user.usertype == "distributor":
                DistributorCompany.objects.create(did=user)  # Create a Distributor instance linked to the user
            elif user.usertype == "customer":
                Customer.objects.create(cid=user)  # Create a Customer instance linked to the user
            elif user.usertype == "agricultural_officer":
                AgriculturalOfficer.objects.create(aid=user)  # Create an AgriculturalOfficer instance linked to the user
            elif user.usertype == "supplier":
                Supplier.objects.create(sid=user)  # Create a Supplier instance linked to the user
            elif user.usertype == "vendor":
                Vendor.objects.create(user=user)  # Create a Vendor instance linked to the user
            else:
                # Handle case where user type is not recognized
                print(f"User type '{user.usertype}' not recognized.")
    #  <option value="neutroshomist" {% if request.POST.usertype == "neutroshomist" %}selected{% endif %}>Neutroshomist</option>
#             <option value="customer" {% if request.POST.usertype == "customer" %}selected{% endif %}>Agricultural Officer</option>
#             <option value="vendor" {% if request.POST.usertype == "vendor" %}selected{% endif %}>Retailer</option>
#             <option value="distributor" {% if request.POST.usertype == "distributor" %}selected{% endif %}>Distributor Company</option>
#             <option value="customer" {% if request.POST.usertype == "customer" %}selected{% endif %}>Customer</option>
#             <option value="warehouse_manager" {% if request.POST.usertype == "warehouse_manager" %}selected{% endif %}>Warehouse Manager</option>
#             <option value="farmer" {% if request.POST.usertype == "farmer" %}selected{% endif %}>Farmer</option>
#             <option value="supplier" {% if request.POST.usertype == "supplier" %}selected{% endif %}>Supplier</option>
#             <option value="vendor" {% if request.POST.usertype == "vendor" %}selected{% endif %}>Vendor</option>

            
                    
        

        except Exception as e:
            # If there is an error with saving the user, return an error message
            return render(request, 'user_signup_form.html', {"text": f"Error saving user: {str(e)}"})

        # If everything is successful, return a success message
        return render(request, 'user_signup_form.html', {"text": "Form submitted successfully!","user":user})

    # If the form is not submitted (GET request), just render the empty form page
    return render(request, 'user_signup_form.html')
