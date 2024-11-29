from django.shortcuts import render
from django.http import HttpResponse

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

        # If no errors, proceed with form processing (e.g., saving to database)
        # Example: Saving user and location data to database (you can add your model logic here)
        # user = User.objects.create(name=name, email=email, password=password, ...)
        # location = Location.objects.create(latitude=latitude, longitude=longitude, altitude=altitude, timezone=timezone, ...)

        # Render a success message with the form data
        return render(request, 'user_signup_form.html', {"text": "Form submitted successfully!"})

    # If the form is not submitted (GET request), just render the empty form page
    return render(request, 'user_signup_form.html')
