from django.urls import path
from . import views

urlpatterns = [
    path('add/<int:id>', views.Add_Cart.as_view()),
    path('detail', views.Cart_Detail.as_view()),
    path('ordercreate', views.order_create.as_view()),
    path('orderdetail', views.Order_Detail.as_view()),
    path('orderuser/<int:id>', views.Order_User.as_view()),

]
