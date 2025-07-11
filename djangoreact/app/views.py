from django.shortcuts import render
from .serializers import ProductSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product

# Create your views here.


@api_view(["GET"])
def Apioverview(req):
    api_urls = {
        "allproducts": "/allproducts",
        "addproduct": "/addproduct",
        "updateproduct": "/updateproduct/update/pk",
        "deleteproduct": "/deleteproduct/delete/pk",
        "search by category": "/searchbycategory/?category=category_name",
    }
    return Response(api_urls)


@api_view(["GET"])
def allproducts(req):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


class AddProduct(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class UpdateProduct(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    partial = True


class DeleteProduct(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
