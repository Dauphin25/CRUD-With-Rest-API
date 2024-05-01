from rest_framework import serializers
from api.models.category import Category
from api.models.item import Item
from api.models.tags import Tag


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):

    def validate(self, data):
        if data['stock'] < 0:
            raise serializers.ValidationError('Stock cannot be negative')

        if data['price'] < 0:
            raise serializers.ValidationError('Price cannot be negative')

        return data

    class Meta:
        model = Item
        fields = '__all__'


class ItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['name', 'price']


class ItemStockUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['stock']
