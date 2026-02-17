from rest_framework import serializers
from .models import Category,Product,Review
from rest_framework.exceptions import ValidationError

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


class CategoryValidateSerializer(serializers.Serializer):
    name = serializers.CharField()

class ProductValidateSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    price = serializers.IntegerField()
    category_id = serializers.IntegerField()
    def validate_category_id(self, category_id):
        try:
            Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            raise ValidationError('Category does not exist')
        return category_id
        
class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField()
    product_id = serializers.IntegerField()
    star = serializers.IntegerField(min_value=1,max_value=10)

    def validate_product_id(self, product_id):
        try:
            Product.objects.get(id=product_id)
        except:
            raise ValidationError('Product  does not exist')
        
