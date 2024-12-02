from django.shortcuts import render
from django.http import HttpResponse
from .models import User,Product, Location,WirehouseManager,Retailer,Farmer,DistributorCompany,Customer,AgriculturalOfficer,Nutritionists,Supplier,Vendor


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





    return render(request,"add_batch_to_invantory.html",{"user":user,"location":location,"product":product})

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
