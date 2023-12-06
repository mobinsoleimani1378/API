from account.models import User
from django.db import models


class Category(models.Model):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='subs', null=True, blank=True)
    title = models.CharField(max_length=30)
    img = models.ImageField(upload_to='images', null=True, blank=True)

    def __str__(self):
        return self.title


class Color(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Size(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='catt', null=True, blank=True)
    title = models.CharField(max_length=30)
    text = models.CharField(max_length=100)
    price = models.CharField(max_length=20)
    img = models.ImageField(upload_to='images', null=True)
    color = models.ManyToManyField(Color, blank=True, related_name='products')
    size = models.ManyToManyField(Size, blank=True, related_name='products')
    review = models.IntegerField(default=0, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commentss')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='comment', null=True, blank=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.fullname


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='like')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}-{self.product}'
