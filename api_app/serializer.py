from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields="__all__"
        

class Product2Serializer(serializers.ModelSerializer):
    name=serializers.CharField()
    description=serializers.CharField()
    price=serializers.DecimalField(max_digits=7, decimal_places=2)
    discount_price=serializers.DecimalField(max_digits=7, decimal_places=2)
    stock=serializers.IntegerField()
    category=serializers.CharField()

    def validate(self, attrs):
        name=attrs.get('name')
        description=attrs['description']
        if name is None:
            raise serializers.ValidationError("name must be provided")
        if description is None:
            raise serializers.ValidationError("please, provide a name")
        return attrs


    def create(self, validated_data):
        return Product.objects.create(
            name=validated_data['name'],
            description=validated_data['description'],
            price=validated_data['price'],
            discount_price=validated_data.get['discount_price'],
            stock=validated_data.get['stock'],
            category=validated_data['category'] 
        )       

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.discount_price = validated_data.get('discount_price', instance.discount_price)
        instance.stock = validated_data.get('stock', instance.stock)
        instance.category = validated_data.get('category', instance.get)
        instance.save()
        return instance    