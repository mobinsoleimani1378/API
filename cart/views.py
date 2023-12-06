from rest_framework.response import Response
from rest_framework.views import APIView
from cart.cart_module import Cart
from cart.models import Order, OrderItem
from cart.serializers import CartSer, OrderSer, OrderItemSer
from product.models import Product


class Add_Cart(APIView):
    def post(self, request, id):
        color = request.data.get('color')
        size = request.data.get('size')
        quantity = request.data.get('quantity')
        product = Product.objects.get(id=id)
        print(color, size)
        cart = Cart(request)
        cart.add(product, color, size, quantity)
        return Response({'add to cart': 'done'})


class Cart_Detail(APIView):
    def get(self, request):
        cart = Cart(request)
        ser = CartSer(instance=cart, many=True)
        return Response(ser.data)


class order_create(APIView):
    def get(self, request):
        cart = Cart(request)
        order = Order.objects.create(user=request.user)
        for item in cart:
            OrderItem.objects.create(order=order, product=item['product'], color=item['color'], size=item['size'],
                                     quantity=item['quantity'], price=item['price'])
        cart.remove_cart()
        return Response({'order': 'ok', 'id': order.id})


class Order_User(APIView):
    def get(self, request, id):
        order = Order.objects.get(id=id)
        ser = OrderSer(instance=order)
        return Response(ser.data)


class Order_Detail(APIView):
    def get(self, request):
        orderitems = OrderItem.objects.all()
        ser = OrderItemSer(instance=orderitems, many=True)
        return Response(ser.data)
