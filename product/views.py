from django.http import request
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.utils import text
from .models import Product, Category

#-------cart----------
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
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
    products = category_info.procategory.all()
    context = {'category_info':category_info, 'products': products}
    return render(request, 'Product/category_detail.html', context)   




#----------cart-----------------



@login_required(login_url="/users/login")
def cart_add(request, id):
    cart = Cart(request)
    product_info = Product.objects.get(id=id)
    cart.add(product_info=product_info)
    return redirect("products:product_list")


@login_required(login_url="/users/login")
def item_clear(request, id):
    cart = Cart(request)
    product_info = Product.objects.get(id=id)
    cart.remove(product_info)
    return redirect("products:cart_detail")


@login_required(login_url="/users/login")
def item_increment(request, id):
    cart = Cart(request)
    product_info = Product.objects.get(id=id)
    cart.add(product_info=product_info)
    return redirect("products:cart_detail")


@login_required(login_url="/users/login")
def item_decrement(request, id):
    cart = Cart(request)
    product_info = Product.objects.get(id=id)
    cart.decrement(product_info=product_info)
    return redirect("products:cart_detail")


@login_required(login_url="/users/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("products:cart_detail")


@login_required(login_url="/users/login")
def cart_detail(request):
    return render(request, 'cart/cart_detail.html')