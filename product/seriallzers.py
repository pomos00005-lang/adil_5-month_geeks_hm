from rest_framework import serializers
from .models import Category,Product,Review

class CategoryListSerializer(serializers.ModelSerializer):
    count = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = 'name count'.split()
    def get_count(self,category):
        return len(category.product_category.all())
class CategoryDetailSerializer(serializers.ModelSerializer):
    count = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = '__all__'

    def get_count(self,category):
        return len(category.product_category.all())

class ProductListSerializer(serializers.ModelSerializer):
    medium_reviews = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = 'title medium_reviews'.split()
    
    def get_medium_reviews(self,product):
        return product.medium_review
    




class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class ProductDetailSerializer(serializers.ModelSerializer):
    reviews = ReviewListSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = '__all__'

class ReviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
