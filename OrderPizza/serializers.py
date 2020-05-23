from rest_framework import serializers

from .models import Regular, Sicilian, Toppings, Subs, SubToppings, Pasta, Salads, Platters

class RegularSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Regular
        fields = ('type', 'smallprice', 'largeprice')

class SicilianSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sicilian
        fields = ('type', 'smallprice', 'largeprice')

class ToppingsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Toppings
        fields = ('topping')

class SubsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = Subs
        fields = ('type', 'smallprice', 'largeprice')

class SubToppingsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SubToppings
        fields = ('type', 'smallprice', 'largeprice')

class PastaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pasta
        fields = ('type', 'price')

class SaladsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Salads
        fields = ('type', 'price')

class PlattersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Platters
        fields = ('type', 'smallprice', 'largeprice')
