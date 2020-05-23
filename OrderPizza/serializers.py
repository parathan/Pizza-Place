from rest_framework import serializers

from .models import Regular, Sicilian, Toppings, Subs, SubToppings, Pasta, Salad, Platters,

class RegularSerializer(serializers.HyperLinkedModelSerializer):
    class Meta:
        model = Regular
        fields = ('type', 'smallprice', 'largeprice')

class SicilianSerializer(serializers.HyperLinkedModelSerializer):
    class Meta:
        model = Sicilian
        fields = ('type', 'smallprice', 'largeprice')

class ToppingsSerializer(serializers.HyperLinkedModelSerializer):
    class Meta:
        model = Toppings
        fields = ('topping')

class SubsSerializer(serializers.HyperLinkedModelSerializer):
    class Meta:
        model  = Subs
        fields = ('type', 'smallprice', 'largeprice')

class SubToppingsSerializer(serializers.HyperLinkedModelSerializer):
    class Meta:
        model = SubToppings
        fields = ('type', 'smallprice', 'largeprice')

class PastaSerializer(serializers.HyperLinkedModelSerializer):
    class Meta:
        model = Pasta
        fields = ('type', 'price')

class SaladsSerializer(serializers.HyperLinkedModelSerializer):
    class Meta:
        model = Salads
        fields = ('type', 'price')

class PlattersSerializer(serializers.HyperLinkedModelSerializer):
    class Meta:
        model = Platters
        fields = ('type', 'smallprice', 'largeprice')

    
