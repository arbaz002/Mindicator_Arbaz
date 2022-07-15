import re
from django.contrib.auth.models import Permission, User, Group
from django.http import request
from rest_framework.serializers import Serializer
from .models import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import (
	viewsets, 
	status, 
	permissions,
	views,
	generics,
	mixins
)

from django.shortcuts import get_object_or_404,render
from .serializers import * 




class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	http_method_names = ['post']

	def create(self,request,*args, **kwargs):
		try:
			post_data = request.data
			new_user = User(username=post_data['username'])
			new_user.set_password(post_data['password'])
			new_user.save()
		except Exception as err:
			return Response(err,status= status.HTTP_400_BAD_REQUEST)
		
		return Response(data = "Account successfully created",status= status.HTTP_200_OK)


class StationViewSet(viewsets.ModelViewSet):
	queryset = Station.objects.all()
	serializer_class = StationSerializer

	def create(self,request,*args, **kwargs):
		try:
			station_data = request.data
			serialized_data = serializer_class(data=station_data)
			serialized_data.save()
		except Exception as err:
			return Response(err,status= status.HTTP_400_BAD_REQUEST)
		
		return Response(data = "New Station successfully added",status= status.HTTP_200_OK)



class TrainViewSet(viewsets.ModelViewSet):
	queryset = Train.objects.all()
	serializer_class = TrainSerializer

	def create(self,request,*args, **kwargs):
		try:
			train_data = request.data
			serialized_data = serializer_class(data=train_data)
			serialized_data.save()
		except Exception as err:
			return Response(err,status= status.HTTP_400_BAD_REQUEST)
		
		return Response(data = "Train successfully added",status= status.HTTP_200_OK)


class StationList(views.APIView):  

	def get(self,request,arrival_station_name,sort_by_arrival_time):
		query = Station.objects.all()
		serializer = StationSerializer(query,many=True)
		return Response(serializer.data)


class TrainList(views.APIView):
  
	def get(self,request,arrival_station_name,sort_by_arrival_time): 
		query = Train.objects.all().filter(arrival_station=Station.objects.get(name=arrival_station_name))

		if sort_by_arrival_time=="true":
			query=query.order_by('arrival_time')

		serializer = TrainSerializer(query,many=True)
		return Response(serializer.data)


@api_view(['POST'])
def verifyUser(request):
    serializer=UserSerializer

    username,password=None,None
    try:
        username=request.data['username']
        password=request.data['password']
        user=authenticate(username=username,password=password)
        if not user:
        	return Response(data = "Username or Password is incorrect",status= status.HTTP_401_UNAUTHORIZED)
    except:
        return Response(data = "Username or Password is Missing",status= status.HTTP_400_BAD_REQUEST)

    return Response(data = "",status= status.HTTP_200_OK)
