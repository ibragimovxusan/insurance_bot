from rest_framework import serializers
from ..models import InsurancePeriod, Account, CarDriver


class InsurancePeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = InsurancePeriod
        fields = '__all__'


class CarDriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarDriver
        fields = '__all__'


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'
