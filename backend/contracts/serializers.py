from .models import Contracts
from rest_framework import serializers


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contracts
        fields = '__all__'
