from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import UserSerializer
from .models import User
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all().order_by('real_name')
	serializer_class = UserSerializer
	def list(self, request, *args, **kwargs):
		instance = self.filter_queryset(self.get_queryset())
		page = self.paginate_queryset(instance)
		if page is not None:
			serializer = self.get_pagination_serializer(page)
		else:
			serializer = self.get_serializer(instance, many=True)
		serializer_data = serializer.data 
		serializer_data = {"members" : serializer_data,"ok":True} 
		return Response(serializer_data) 