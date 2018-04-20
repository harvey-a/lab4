from models import User, Product, Cart
from serializers import UserSerializer, ProductSerializer, CartSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import  generics
from rest_framework.views import APIView
from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.shortcuts import render
from rest_framework import status

# Create your views here.

class UserList(APIView):
	def get(self,request):
		users = User.objects.all()
		serialized_account = UserSerializer(users,many=True)
		return Response(serialized_account.data)

	def post(self, request):
		data = JSONParser().parse(request)
		serializer = UserSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=201)

class UserDetail(APIView):
	def get_object(self, pk):
		try:
			return User.objects.get(pk=pk)
		except User.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		user = self.get_object(pk)
		serializer = UserSerializer(user)
		return Response(serializer.data)

	def put(self, request, pk, format=None):
		user = self.get_object(pk)
		serializer = UserSerializer(user, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		user = self.get_object(pk)
		user.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

class ProductList(APIView):
	def get(self,request):
		users = Product.objects.all()
		print(users)
		serialized_account = ProductSerializer(users,many=True)
		return Response(serialized_account.data)

	def post(self, request):
		data = JSONParser().parse(request)
		serializer = ProductSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=201)

class ProductDetail(APIView):
	def get_object(self, pk):
		try:
			return Product.objects.get(pk=pk)
		except Product.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		user = self.get_object(pk)
		serializer = ProductSerializer(user)
		return Response(serializer.data)

	def put(self, request, pk, format=None):
		user = self.get_object(pk)
		serializer = ProductSerializer(user, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		user = self.get_object(pk)
		user.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

class CartList(APIView):
	def get(self,request):
		users = Cart.objects.all()
		print(users)
		serialized_account = CartSerializer(users,many=True)
		return Response(serialized_account.data)

	def post(self, request):
		data = JSONParser().parse(request)
		serializer = CartSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=201)

class CartDetail(APIView):
	def get_object(self, pk):
		try:
			return Cart.objects.get(pk=pk)
		except Product.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		user = self.get_object(pk)
		serializer = CartSerializer(user)
		return Response(serializer.data)

	def put(self, request, pk, format=None):
		user = self.get_object(pk)
		serializer = CartSerializer(user, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk):
		user = self.get_object(pk)
		user.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)