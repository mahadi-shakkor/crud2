from rest_framework import serializers
from .models import HarvestFields

class HarvestFieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HarvestFields
        fields = ['fields_id', 'userid']  # Include other fields if needed
