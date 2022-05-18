from django.shortcuts import render
from django.http import Http404
from .models import Brand_Product, Model_Product, Product, Type_Operation, Company
# Create your views here.
def index(request):
    return render(request, 'table.html')