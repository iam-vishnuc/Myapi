from app.serializers import ProductSerializer,CategorySerializer
from app.models import Product,Category
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def viewcategory(request):
    category = Category.objects.all()
    serializer = CategorySerializer(category, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def viewproduct(request):
    product = Product.objects.all()
    serializer = ProductSerializer(product, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def createproduct(request):
    serialiser =  ProductSerializer(data = request.data)
    if serialiser.is_valid():
        serialiser.save()

    return Response(serialiser.data)


@api_view(['POST'])
def createcategory(request):
    serialiser =  CategorySerializer(data = request.data)
    if serialiser.is_valid():
        serialiser.save()

    return Response(serialiser.data)

@api_view(['DELETE'])
def delete_product(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)