from django.shortcuts import render
from django.forms.models import model_to_dict
from django.http import JsonResponse
from .models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import ProductSerializer
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status
from .serializer import ProductSerializer, Product2Serializer
from rest_framework.generics import ListAPIView,ListCreateAPIView, RetrieveAPIView, DestroyAPIView, RetrieveUpdateAPIView
from rest_framework.exceptions import ValidationError

# Create your views here.
def first_api_view(request):
    data = {
        "name":"jibola",
        "occupation":"developer"
    }
    return JsonResponse(data)


@api_view (['GET'])
def second_api_view(request):
    #get a model instance
    product = Product.objects.get(id=1)
    # data = {}
    # if product:
    #     data['name']=product.name
    #     data['description']=product.description

    if product:
        data=model_to_dict(product)
    #return JsonResponse(data)
    return Response(data, status=200)

@api_view(['GET'])
def get_all_product(request):
    all_product=Product.objects.all()
    serializer=ProductSerializer(all_product, many=True)
    print(serializer)
    return Response(serializer.data, status=200)
    # data={
    #     'product': all_product
    # }
    # return Response(data, status=200)

class GetAllProductView(APIView):
    def get(self, request, *args, **kwargs):
        products=Product.objects.all()
        serializer=ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data= request.data
        serializer=ProductSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

###GENERIC API VIEW ###

class AllProductView(ListAPIView):
    serializer_class=ProductSerializer
    queryset = Product.objects.all()

    def get_queryset(self):
        queryset=self.queryset.filter(category__icontaina='items')
        return queryset

    def get_queryset(self):
        queryset= self.queryset.filter(name__startswith='s')
        return queryset
    
def send_user_email():
        print('send email after product is save')

class GetProductCategoryView(APIView):
    def get(self, request, cat):
        products=Product.objects.filter(category=cat)
        serializer=ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class AllProductCreateView(ListCreateAPIView):
    user="admin"
    serializer_class=ProductSerializer
    queryset=Product.objects.all()

    def perform_create(self, serializer):
        print(serializer.data)
        if self.user != "admin":
            raise ValidationError("only admin can add new product")
        serializer.save()
        send_user_email()

class ProductDetail2(RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class AllProductUpdateView(RetrieveUpdateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class DeleteProduct(DestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class ProductDetail(APIView):
    pass
    ### to pass
    def get_object(self, pk):  
        try:
            product=Product.objects.get(id=pk)
            return product
        except Product.DoesNotExist:
            raise Http404

    def get(self, requets, *args, **kwargs):
        product=self.get_object(kwargs.get('pk'))
        serializer=ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        product=self.get_objects(pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product=self.get_object(pk)
        product.delete()
        return Response({'message': 'item deleted successfully'}, status=status.HTTP_200_OK)  
