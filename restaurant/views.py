from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from .models import Menu
from .serializers import MenuSerializer

# Create your views here.
def index(request):
    return render(
        request,
        'index.html',
        {}
    )
    

class MenuMixin():
    def get_queryset(self):
        return Menu.objects.all()
    
    def get_serializer_class(self):
        return MenuSerializer
    

class MenuItemView(MenuMixin, ListCreateAPIView): pass
class SingleMenuItemView(MenuMixin, RetrieveUpdateAPIView, DestroyAPIView): pass