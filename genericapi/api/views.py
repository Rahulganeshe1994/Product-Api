from django.shortcuts import render
from api .models import Product
from api .serializers import ProductSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,DestroyModelMixin,UpdateModelMixin
# Create your views here.


class Productapi(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset =Product.objects.all()
    serializer_class = ProductSerializer
    
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    
    
class Productcrudapi(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset =Product.objects.all()
    serializer_class = ProductSerializer
    
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs) 
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs) 
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs) 