from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.product_list),
    path('<int:id>',views.product_detail),


] 