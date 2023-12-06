from django.contrib import admin
from .models import Product, Color, Size, Category, Comment, Like

admin.site.register(Product)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Like)
