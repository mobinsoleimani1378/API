from django.urls import path
from . import views

urlpatterns = [
    path('list', views.Productlist.as_view()),
    path('detail/<int:id>', views.ProductDetail.as_view()),
    path('filter', views.Product_Filter.as_view()),
    path('comment/<int:id>', views.CommentView.as_view()),
    path('like/<int:id>', views.Like_user.as_view()),
    path('add', views.ProductAdd.as_view()),

]
