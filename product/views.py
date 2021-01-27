from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Product
# Create your views here.



def product_list(request):
    all_product = Product.objects.all()
    paginator = Paginator(all_product, 8)

    page_number = request.GET.get('page')
    all_product = paginator.get_page(page_number)
    context = {'all_product' : all_product}
    return render(request, 'Product/product_list.html', context)


def product_detail(request, slug):
    product_info = Product.objects.get(PROslug=slug)
    context = {'product_info' : product_info}
    return render(request, 'Product/product_detail.html', context)