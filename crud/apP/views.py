from django.shortcuts import render
from django.http import HttpResponse
from .models import Batch,User,Product, Location,WirehouseManager,Retailer,Farmer,DistributorCompany,Customer,AgriculturalOfficer,Nutritionists,Supplier,Vendor


from django.shortcuts import render
from django.http import HttpResponse
from .models import User
def add_batch_to_invantory(request):
    userid = request.GET.get('userid')
    
    try:
        user = User.objects.get(userid=userid)
        location=user.location
        product=Product.objects.all()
    except:
        return HttpResponse("user not found")
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
        print("Form data received:")
        print(f"Product ID: {product_id}")
        print(f"Sell: {sell}")
        print(f"Store: {stor}")
        print(f"Temperature: {temperature}")
        print(f"Humidity: {humidity}")
        print(f"Batch count: {batch_count}")
        print(f"DateTime: {datetime_value}")
        print(f"Unit: {unit}")
        print(f"Per unit price: {per_unit_price}")
        print(f"Description: {description}")
        print(f"Product amount per batch: {product_amount}")
        print(f"Location: {street}, {city}, {state}, {country}")
        print(f"Latitude: {latitude}")
        print(f"Longitude: {longitude}")
        print(f"Altitude: {altitude}")
        print(f"Timezone: {timezone}")

        # Validate required fields
        # errors = []
        # if not product_id:
        #     errors.append("Product selection is required.")
        # if not humidity or not 0 <= float(humidity) <= 100:
        #     errors.append("Humidity must be between 0 and 100%.")
        # if not temperature or not -50 <= float(temperature) <= 50:
        #     errors.append("Temperature must be between -50°C and 50°C.")
        # if not batch_count or int(batch_count) < 1:
        #     errors.append("Batch count must be at least 1.")
        # if not per_unit_price or float(per_unit_price) <= 0:
        #     errors.append("Per unit price must be a positive number.")
        # if not product_amount or float(product_amount) <= 0:
        #     errors.append("Product amount per batch must be a positive number.")
        # if not street or not city or not state or not country:
        #     errors.append("Complete location details (street, city, state, country) are required.")

        # if errors:
        #     return render(
        #         request,
        #         "add_batch_to_invantory.html",
        #         {
        #             "errors": errors,
        #             "user": user,
        #             "location": location,
        #             "user":user,"location":location,"product":product
                    
        #         },
        #     )

        # Process and save the valid data (this is a placeholder; customize as needed)
        # Example:
        # InventoryEntry.objects.create(
        #     user=user,
        #     product_id=product_id,
        #     sell=bool(sell),
        #     stor=bool(stor),
        #     temperature=temperature,
        #     humidity=humidity,
        #     batch_count=batch_count,
        #     datetime=datetime_value,
        #     unit=unit,
        #     per_unit_price=per_unit_price,
        #     description=description,
        #     product_amount=product_amount,
        #     street=street,
        #     city=city,
        #     state=state,
        #     country=country,
        #     latitude=latitude,
        #     longitude=longitude,
        #     altitude=altitude,
        #     timezone=timezone,
        # )


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
            product = Product.objects.get(product_id=int(product_id))
            
            # Assuming you have valid Location, Product, User, and Harvest objects with corresponding IDs.
            location = Location.objects.get(id=1)  # Replace with valid Location ID
            product = Product.objects.get(id=10)  # Replace with valid Product ID
            user = User.objects.get(id=1)  # Replace with valid User ID
            # harvest = Harvest.objects.get(id=1)  # Replace with valid Harvest ID

            # Create a new Batch entry
            batch = Batch.objects.create(
                location=location,  # Location foreign key
                sid=None,  # SID foreign key, you can set this to None if not applicable
                market=None,  # MARKET_ID foreign key, you can set this to None if not applicable
                product_amount=100.00,  # Product Amount
                sell=True,  # SELL as True (1)
                store=True,  # STORE as True (1)
                optimum_temperature_to_store=25.00,  # Optimum Temperature
                optimum_humidity_to_store=60.00,  # Optimum Humidity
                product_unit_price=15.50,  # Product Unit Price
                kg='KG',  # Example Unit for KG (can be None or another unit if needed)
                ton='TON',  # Example Unit for TON (can be None or another unit if needed)
                mon='MON',  # Example Unit for MON (can be None or another unit if needed)
                batch_description='Batch description text',  # Description of the batch
                date_time_batch_created=datetime.now(),  # Current datetime
                user=user,  # User foreign key
                product=product  # Product foreign key
                # hid=harvest,  # Harvest foreign key
            )

            print("Batch created:", batch)

            
        except Exception as e:
            # If there is an error with saving the location, return an error message
            return render(request, 'add_batch_to_invantory.html', {"text": f"Error saving location: {str(e)}","user":user,"location":location,"product":product})

        return render(request, 'add_batch_to_invantory.html', {"text": "batch added successfully!","user":user,"location":location,"product":product})






    return render(request,"add_batch_to_invantory.html",{"user":user,"location":location,"product":product})
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
