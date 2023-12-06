from product.models import Product


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}

        self.cart = cart

    def __iter__(self):
        cart = self.cart.copy()

        for item in cart.values():
            product = Product.objects.get(id=int(item['id']))
            item['title'] = product.title
            item['product'] = product
            item['image'] = product.img.url
            item['total'] = int(item['quantity']) * int(item['price'])
            item['unique_id'] = self.unique_key(product.id, item['color'], item['size'])
            yield item

    def unique_key(self, id, color, size):
        result = f'{id}-{color}-{size}'
        return result

    def add(self, product, color, size, quantity):
        unique = self.unique_key(product.id, color, size)
        if unique not in self.cart:
            self.cart[unique] = {'quantity': 0, 'price': str(product.price), 'color': color, 'size': size,
                                 'id': product.id}
        self.cart[unique]['quantity'] += int(quantity)
        self.save()

    def save(self):
        self.session.modified = True

    def total(self):
        total = 0
        for item in self.cart.values():
            total = total + item['total']
        return total

    def remove_cart(self):
        del self.session['cart']

    def delete(self, id):
        if id in self.cart:
            del self.cart[id]
            self.save()

    def all_quantity(self):
        quantity = 0
        for item in self.cart.values():
            quantity = quantity + int(item['quantity'])
        return quantity
