from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
# Create your views here.

class UsersignUpViewSet(ViewSet):
    def create(self,request):
        dser=UserSerializer(data=request.data)
        if dser.is_valid():
            dser.save()
            return Response(data=dser.data,status=status.HTTP_201_CREATED)
        return Response(data=dser.errors,status=status.HTTP_400_BAD_REQUEST)
    
class CustomerViewSet(ModelViewSet):
    queryset=Customer
    serializer_class=CustomerSerializer
    authentication_classes=TokenAuthentication
    permission_classes=IsAuthenticated

    def perform_create(self, serializer):
        return serializer.save(mechanic=self.request.user)
    
    def get_queryset(self):
        return self.queryset.filter(mechanic=self.request.user)
    
    @action(methods="POST",detail=True)
    def addservices(self,request,pk=0):
        customer=self.get_object()
        dser=Serviceserializer(data=request.data)
        if dser.is_valid():
            dser.save(customer=customer)
            return Response(data=dser.data,status=status.HTTP_201_CREATED)
        return Response(data=dser.error,status=status.HTTP_400_BAD_REQUEST)
    
    @action(methods="POST",detail=True)
    def servicelist(self,request,pk=0):
        customer=self.get_object
        services=Services.objects.filter(customer=customer)
        ser=Serviceserializer(services,many=True)
        return Response(data=ser.data,status=status.HTTP_200_OK)
    
class ServiceViewSet(ViewSet):
    permission_classes=IsAuthenticated
    authentication_classes=TokenAuthentication

    def partial_update(self,request,pk=0):
        services=Services.objects.get(id=pk)
        dser=Serviceserializer(data=request.data,partial=True)
        if dser.is_valid():
            dser.save()
            return Response(data=dser.data,status=status.HTTP_200_OK)
        return Response(data=dser.error,status=status.HTTP_400_BAD_REQUEST)
