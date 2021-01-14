from django.shortcuts import render
from .models import Product
# Create your views here.



def product_list(request):
    all_product = Product.objects.all()
    context = {'all_product' : all_product}
    return render(request, 'Product/product_list.html', context)


def product_detail(request, id):
    product_info = Product.objects.get(id=id)
    context = {'product_info' : product_info}
    return render(request, 'Product/product_detail.html', context)