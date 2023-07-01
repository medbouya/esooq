from rest_framework import serializers
from .models import Country, City, Category, Subcategory, Ad, Image, Tag


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['name', ]

class CitySerializer(serializers.ModelSerializer):
    country = CountrySerializer()  # Serializer for the related 'Country' model

    class Meta:
        model = City
        fields = ['name', 'country']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'image', ]


class SubcategorySerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Subcategory
        fields = ['name', 'category', ]


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['image', ]


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name', ]


class AdSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)
    tags = TagSerializer(many=True)
    location = CitySerializer()
    subcategory = SubcategorySerializer()

    class Meta:
        model = Ad
        fields = ['title', 'description', 'price', 'location', 'subcategory', 'tags', 'images',]

