from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse

def user_siunup_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        usercontactnumber = request.POST.get('usercontactnumber')
        usertype = request.POST.get('usertype')
        street = request.POST.get('street')
        city = request.POST.get('city')
        state = request.POST.get('state')
        country = request.POST.get('country')
        return HttpResponse(f"Form submitted successfully! Name: {name}, Email: {email}, User Type: {usertype}")
    return render(request, 'user_siunup_form.html')

