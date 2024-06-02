from rest_framework import serializers
# from .models import ExchangeRates
from .models import Exchange


class ExchangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exchange
        fields = '__all__'
        read_only_fields = ('req_dt',)


# class ExchangeRatesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ExchangeRates
#         fields = '__all__'
#         read_only_fields = ('req_dt',)
