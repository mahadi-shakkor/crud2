from django import forms

from django import forms
from datetime import datetime

class PDemandForm(forms.Form):
    product = forms.IntegerField(required=False, widget=forms.HiddenInput())  # Assuming foreign key id for simplicity
    userid = forms.IntegerField(required=False, widget=forms.HiddenInput())  # Assuming foreign key id for simplicity
    locationid = forms.IntegerField(required=False, widget=forms.HiddenInput())  # Assuming foreign key id for simplicity
    p_demand_id = forms.IntegerField(widget=forms.HiddenInput())  # Primary key hidden
    demandamount = forms.DecimalField(max_digits=10, decimal_places=2, required=True)
    ton = forms.DecimalField(max_digits=10, decimal_places=2, required=False)
    mon = forms.DecimalField(max_digits=10, decimal_places=2, required=False)
    kg = forms.DecimalField(max_digits=10, decimal_places=2, required=False)
    demand_date_time = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        required=True
    )
    city = forms.CharField(max_length=100, required=False)
    state = forms.CharField(max_length=100, required=False)
    area = forms.CharField(max_length=255, required=False)
    season = forms.CharField(max_length=50, required=False)
    price_should_be = forms.DecimalField(max_digits=10, decimal_places=2, required=False)
    status = forms.CharField(max_length=50, required=False)
    comments = forms.CharField(widget=forms.Textarea, required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set default datetime to current time
        self.fields['demand_date_time'].initial = datetime.now().strftime('%Y-%m-%dT%H:%M')

