from django import forms
from .models import PDemand, Product  # Import the related Product model

class PDemandForm(forms.ModelForm):
    class Meta:
        model = PDemand
        fields = [
            'product', 
            'demandamount', 
            'ton', 
            'mon', 
            'kg', 
            'demand_date_time', 
            'city', 
            'state', 
            'area', 
            'season', 
            'price_should_be', 
            'status', 
            'comments'
        ]  # Exclude 'userid' and 'locationid'
        widgets = {
            'demand_date_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'comments': forms.Textarea(attrs={'rows': 3}),
        }
    
    def __init__(self, *args, **kwargs):
        self.userid = kwargs.pop('userid', None)
        self.locationid = kwargs.pop('locationid', None)
        super().__init__(*args, **kwargs)
        
        # Customize the product field to display product names in the dropdown
        self.fields['product'].queryset = Product.objects.all()
        self.fields['product'].label_from_instance = lambda obj: obj.product_name  # Assuming `name` is the field for product name

    def save(self, commit=True):
        instance = super().save(commit=False)
        # Manually set `userid` and `locationid` if provided
        if self.userid:
            instance.userid_id = self.userid
        if self.locationid:
            instance.locationid_id = self.locationid
        if commit:
            instance.save()
        return instance




from django import forms
from .models import Location

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
