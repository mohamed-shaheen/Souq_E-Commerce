from django.urls import path, include
from . import views

app_name = 'product'


urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<slug:slug>',views.product_detail, name='product_detail'),
    path('category/<slug:slug>', views.category_pages, name='cat_detail')


] 