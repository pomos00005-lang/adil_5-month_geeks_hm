from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .seriallzers import (CategoryListSerializer,CategoryDetailSerializer,ProductListSerializer,ProductDetailSerializer,ReviewListSerializer,ReviewDetailSerializer,
                          ReviewValidateSerializer,ProductValidateSerializer,CategoryValidateSerializer)
from .models import Category,Product,Review
from django.db import transaction


#CATEGORY LIST

@api_view(['GET','POST'])
def category_list_api_view(req):
    if req.method == 'GET':
        category_list = Category.objects.all()

        data = CategoryListSerializer(category_list,many=True).data

        return Response(data=data)

    elif req.method == 'POST':
        serializer = CategoryValidateSerializer(data=req.data)
        serializer.is_valid(raise_exception=True)

        name = serializer.validated_data.get('name')
        with transaction.atomic():
            category = Category.objects.create(name=name)

        return Response(status=status.HTTP_201_CREATED,
                        data=CategoryDetailSerializer(category).data)

#CATEGORY DETAIL

@api_view(['GET','PUT','DELETE'])
def category_detail_api_view(req,id):
    try:
        category = Category.objects.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error':'category not found!'})
    if req.method == 'GET':
            
        data = CategoryDetailSerializer(category,many=False).data
        return Response(data=data)
    
    elif req.method == 'PUT':
        serializer = CategoryValidateSerializer(data=req.data)
        serializer.is_valid(raise_exception=True)

        category.name = serializer.validated_data.get('name')
        category.save()
        return Response(status=status.HTTP_201_CREATED,
                        data=CategoryDetailSerializer(category).data)
    elif req.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_200_OK)

#PRODUCT LIST

@api_view(['GET','POST'])
def product_list_api_view(req):
    if req.method == 'GET':
        product_list = Product.objects.all()

        data = ProductListSerializer(product_list,many=True).data

        return Response(data=data)
    
    elif req.method == 'POST':

        serializer = ProductValidateSerializer(data=req.data)
        serializer.is_valid(raise_exception=True)

        title = serializer.validated_data.get('title')
        description = serializer.validated_data.get('description')
        price = serializer.validated_data.get('price')
        category_id = serializer.validated_data.get('category_id')
        with transaction.atomic():
            product = Product.objects.create(
                title=title,
                description=description,
                price=price,
                category_id=category_id
            )
        return Response(status=status.HTTP_201_CREATED,
                        data=ProductDetailSerializer(product).data)


#PRODUCT DETAIL

@api_view(['GET','PUT','DELETE'])
def product_detail_api_view(req,id):
    try:
        product = Product.objects.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error':'product not found!'})
    if req.method == 'GET':
        data = ProductDetailSerializer(product,many=False).data
        return Response(data=data)
    elif req.method == 'PUT':

        serializer = ProductValidateSerializer(data=req.data)
        serializer.is_valid(raise_exception=True)



        product.title = serializer.validated_data.get('title')
        product.description = serializer.validated_data.get('description')
        product.price = serializer.validated_data.get('price')
        product.category_id = serializer.validated_data.get('category_id')
        product.save()
        return Response(status=status.HTTP_201_CREATED,
                        data=ProductDetailSerializer(product).data)
    elif req.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#REVIEW LIST

@api_view(['GET','POST'])
def review_list_api_view(req):
    if req.method == 'GET':
        review_list = Review.objects.all()
        data = ReviewListSerializer(review_list,many=True).data
        return Response(data=data)
    
    elif req.method == 'POST':
        serailizer = ReviewValidateSerializer(data=req.data)
        serailizer.is_valid(raise_exception=True)

        text = serailizer.validated_data.get('text')
        product_id = serailizer.validated_data.get('product_id')
        star = serailizer.validated_data.get('star')
        with transaction.atomic():
            product = Review.objects.create(
                text=text,
                product_id=product_id,
                star=star
            )
        return Response(status=status.HTTP_201_CREATED,
                        data=ReviewDetailSerializer(product).data)

#REVIEWS DETAIL

@api_view(['GET','PUT','DELETE'])
def review_detail_api_view(req,id):
    try:
        review = Review.objects.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error':'review not found!'})
    
    if req.method == 'GET':
        data = ReviewDetailSerializer(review,many=False).data
        return Response(data=data)
    
    elif req.method == 'PUT':
        serailizer = ReviewValidateSerializer(data=req.data)
        serailizer.is_valid(raise_exception=True)

        review.text = serailizer.validated_data.get('text')
        review.product_id = serailizer.validated_data.get('product_id')
        review.star = serailizer.validated_data.get('star')
        review.save()
        return Response(status=status.HTTP_200_OK,
                        data=ReviewDetailSerializer(review).data)
    
    elif req.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)