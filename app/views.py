from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from . serializers import DrinkSerializer
from . models import Drink
from rest_framework.decorators import api_view
@api_view(['GET','POST'])
# Create your views here.
def drink_list(request):
    if request.method=='GET':

        drinks=Drink.objects.all()
        serialier= DrinkSerializer(drinks,many=True)
        return Response( {"dinks":serialier.data}) 
    if request.method=='POST':
        serialier=DrinkSerializer(data=request.data)
        if serialier.is_valid():
            serialier.save()
            return Response (serialier.data,status=status.HTTP_201_CREATED)
@api_view(['GET','PUT','DELETE'])
def drink_detail(request,id):
    try:
        drink = Drink.objects.get(pk=id)
    except Drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method=='GET':
        serializer= DrinkSerializer(drink)
        return Response (serializer.data)
    elif request.method=='PUT':
        serialier=DrinkSerializer(drink,data=request.data)
        if serialier.is_valid():
            serialier.save()
            return Response(serialier.data)
        return Response (serialier.data,status=status.HTTP_201_CREATED)
    elif request.method=='DELETE':
        drink.delete()
        return Response({"message": "Drink deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

