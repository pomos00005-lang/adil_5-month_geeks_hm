from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .seriallzers import CategoryListSerializer,CategoryDetailSerializer,ProductListSerializer,ProductDetailSerializer,ReviewListSerializer
from .models import Category,Product,Review

#CATEGORY LIST

@api_view(['GET'])
def category_list_api_view(req):
    category_list = Category.objects.all()

    data = CategoryListSerializer(category_list,many=True).data

    return Response(data=data)

#CATEGORY DETAIL

@api_view(['GET'])
def category_detail_api_view(req,id):
    try:
        category = Category.objects.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error':'category not found!'})
    
    data = CategoryDetailSerializer(category,many=False).data
    return Response(data=data)

#PRODUCT LIST

@api_view(['GET'])
def product_list_api_view(req):
    product_list = Product.objects.all()

    data = ProductListSerializer(product_list,many=True).data

    return Response(data=data)

#PRODUCT DETAIL

@api_view(['GET'])
def product_detail_api_view(req,id):
    try:
        product = Product.objects.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error':'product not found!'})
    
    data = ProductDetailSerializer(product,many=False).data
    return Response(data=data)

#REVIEW LIST

@api_view(['GET'])
def review_list_api_view(req):
    review_list = Review.objects.all()

    data = ReviewListSerializer(review_list,many=True).data

    return Response(data=data)

#REVIEWS DETAIL

@api_view(['GET'])
def review_detail_api_view(req,id):
    try:
        review = Review.objects.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error':'review not found!'})
    
    data = ReviewDetailDetailSerializer(review,many=False).data
    return Response(data=data)
