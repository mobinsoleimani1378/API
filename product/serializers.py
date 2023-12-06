from rest_framework import serializers

from product.models import Product, Category, Comment


class ProductSer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='title', read_only=True)

    class Meta:
        model = Product
        fields = ('title', 'category', 'text', 'price',)


class CategorySer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title',)


class CommentSer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='fullname', read_only=True)

    class Meta:
        model = Comment
        fields = ('body', 'user', 'product',)
