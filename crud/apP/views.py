from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Location

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

        except Exception as e:
            # If there is an error with saving the user, return an error message
            return render(request, 'user_signup_form.html', {"text": f"Error saving user: {str(e)}"})

        # If everything is successful, return a success message
        return render(request, 'user_signup_form.html', {"text": "Form submitted successfully!","user":user})

    # If the form is not submitted (GET request), just render the empty form page
    return render(request, 'user_signup_form.html')
