

from django import forms
from .models import Location
from django import forms
from .models import Product
from datetime import datetime

class ProductDemandForm(forms.Form):
    product = forms.ChoiceField(choices=[], required=True, label="Select Product")
    demandamount = forms.DecimalField(max_digits=10, decimal_places=2, required=True, label="Demand Amount")
    demand_date_time = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}), required=True, label="Demand Date and Time")   
    area = forms.CharField(max_length=255, required=False, label="Area")
    season = forms.CharField(max_length=50, required=False, label="Season")
    price_should_be = forms.DecimalField(max_digits=10, decimal_places=2, required=False, label="Price Should Be")
    status = forms.CharField(max_length=50, required=False, label="Status")
    comments = forms.CharField(widget=forms.Textarea, required=False, label="Comments")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Set the initial value for 'demand_date_time' to the current date and time
        initial = kwargs.get('initial', {})
        initial['demand_date_time'] = datetime.now().strftime('%Y-%m-%dT%H:%M')  # Format for datetime-local input
        kwargs['initial'] = initial
        
        # Query all product names and populate the choices
        product_choices = [(product.product_id, product.product_name) for product in Product.objects.all()]
        self.fields['product'].choices = product_choices

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = [
            'latitude',
            'longitude',
            'street',
            'city',
            'state',
            'country',
            'postalcode',
            'altitude',
            'timezone',
        ]
        widgets = {
            'latitude': forms.NumberInput(attrs={'step': 0.000001}),
            'longitude': forms.NumberInput(attrs={'step': 0.000001}),
            'street': forms.TextInput(attrs={'placeholder': 'Enter street name'}),
            'city': forms.TextInput(attrs={'placeholder': 'Enter city'}),
            'state': forms.TextInput(attrs={'placeholder': 'Enter state'}),
            'country': forms.TextInput(attrs={'placeholder': 'Enter country'}),
            'postalcode': forms.TextInput(attrs={'placeholder': 'Enter postal code'}),
            'altitude': forms.NumberInput(attrs={'placeholder': 'Enter altitude'}),
            'timezone': forms.TextInput(attrs={'placeholder': 'Enter timezone'}),
        }
        labels = {
            'latitude': 'Latitude',
            'longitude': 'Longitude',
            'street': 'Street',
            'city': 'City',
            'state': 'State',
            'country': 'Country',
            'postalcode': 'Postal Code',
            'altitude': 'Altitude',
            'timezone': 'Timezone',
        }
