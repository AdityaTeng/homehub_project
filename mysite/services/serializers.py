from rest_framework import serializers
from . import models

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Request
        fields = ('id', 'request_type', 'request_description', 'city', 'state', 'pincode', 'alt_phone', 'timestamp')