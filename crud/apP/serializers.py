from rest_framework import serializers
from .models import *

class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields='__all__'




class HarvestFieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HarvestFields
        fields = ['fields_id', 'userid']  # Include other fields if needed
