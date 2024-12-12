from rest_framework import serializers
from .models import *

class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields='__all__'

    def validate(self, data):
        if data['age']<18:
            raise serializers.ValidationError('Age have to be gretter than 18')
        special_characters = "!@#$%^&*()-+?_=,<>/"
        if any(c in special_characters for c in data['name']):
            raise serializers.ValidationError("Name cannot contain special characters.")

        return data




class HarvestFieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HarvestFields
        fields = ['fields_id', 'userid']  # Include other fields if needed
