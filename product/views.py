from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination

from account.models import User
from product.models import Product, Category, Comment, Like
from product.serializers import ProductSer, CategorySer, CommentSer
from .permissions import SellerPer, IsUserOrReadOnly
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class Productlist(APIView):
    def get(self, request):
        products = Product.objects.all()
        paginator = PageNumberPagination()
        result = paginator.paginate_queryset(queryset=products, request=request)
        ser = ProductSer(instance=result, many=True)
        return Response(ser.data)


class ProductDetail(APIView):
    def get(self, request, id):
        products = Product.objects.get(id=id)
        ser = ProductSer(instance=products)
        return Response(ser.data)


class ProductAdd(APIView):
    permission_classes = [SellerPer, IsAuthenticated]

    def post(self, request):
        ser = ProductSer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({'product': 'done'})


class Product_Filter(APIView):
    def get(self, request):
        product = Product.objects.all()
        categories = Category.objects.all()
        categorys = []
        for i in categories:
            if not i.parent:
                if i.catt.all():
                    categorys.append(i)
        cat = request.data.getlist('cat')
        colors = request.data.getlist('color')
        sizes = request.data.getlist('size')
        min_price = request.data.get('min_price')
        max_price = request.data.get('max_price')

        if cat:
            product = product.filter(category__title__in=cat).distinct()

        if min_price and max_price:
            product = product.filter(price__gte=min_price, price__lte=max_price).distinct()
        if colors:
            product = product.filter(color__title__in=colors).distinct()
        if sizes:
            product = product.filter(size__title__in=sizes).distinct()

        paginator = PageNumberPagination()
        result = paginator.paginate_queryset(queryset=product, request=request)

        ser1 = ProductSer(instance=result, many=True)

        return Response(ser1.data)


class CommentView(APIView):
    def get(self, request, id):
        product = Product.objects.get(id=id)
        comments = product.comments.all()
        ser = CommentSer(instance=comments, many=True)
        return Response(ser.data)


class Like_user(APIView):
    def get(self, request, id):
        try:
            like = Like.objects.get(user_id=request.user.id, product_id=id)
            like.delete()
            return Response({'like': 'delete'})
        except:
            Like.objects.create(user_id=request.user.id, product_id=id)
            return Response({'like': 'create'})
