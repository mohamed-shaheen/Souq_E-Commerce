from django.http import request
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.utils import text
from .models import Product, Category
# Create your views here.



def product_list(request):
    all_product = Product.objects.all()
    categories = Category.objects.all()
    num = 8
    if 'searchbar' in request.GET:
        name = request.GET['searchbar']
        if name:
            all_product = all_product.filter(PROname__icontains=name)
            num = len(all_product)

    paginator = Paginator(all_product, num)

    page_number = request.GET.get('page')
    all_product = paginator.get_page(page_number)
    context = {'all_product' : all_product, 'categories':categories}
    return render(request, 'Product/product_list.html', context)


def product_detail(request, slug):
    #product_info = Product.objects.get(PROslug=slug)
    product_info = get_object_or_404(Product, PROslug=slug)
    context = {'product_info' : product_info}
    return render(request, 'Product/product_detail.html', context)


def category_pages(request, slug):
    category_info = get_object_or_404(Category, CATslug=slug)
    #pro = Product.objects.filter(Category__CATname__icontains=)
    context = {'category_info':category_info}
    return render(request, 'category/category_detail.html', context)    