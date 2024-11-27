from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from api.models import Product, Review, Order, OrderItem, ShippingAddress
from api.serializers import (
    UserSerializer,
    UserSerializerWithToken,
    ReviewSerializer,
    ProductSerializer,
    ShippingAddressSerializer,
    OrderItemSerializer,
    OrderSerializer,
)

class UserSerializerTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='testuser@example.com', password='password')

    def test_user_serializer(self):
        serializer = UserSerializer(instance=self.user)
        data = serializer.data
        self.assertEqual(data['username'], self.user.username)
        self.assertEqual(data['email'], self.user.email)
        self.assertEqual(data['name'], self.user.first_name or self.user.email)
        self.assertEqual(data['isAdmin'], self.user.is_staff)

class UserSerializerWithTokenTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='testuser@example.com', password='password')

    def test_user_serializer_with_token(self):
        serializer = UserSerializerWithToken(instance=self.user)
        data = serializer.data
        self.assertIn('token', data)
        self.assertEqual(data['username'], self.user.username)
        self.assertTrue(isinstance(data['token'], str) and len(data['token']) > 10)

class ProductSerializerTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='testuser@example.com', password='password')
        self.product = Product.objects.create(
            user=self.user,
            name="Test Product",
            brand="Test Brand",
            category="Test Category",
            description="Test Description",
            rating=4.5,
            numReviews=10,
            price=100.00,
            countInStock=5,
        )

    def test_product_serializer(self):
        serializer = ProductSerializer(instance=self.product)
        data = serializer.data
        self.assertEqual(data['name'], self.product.name)
        self.assertEqual(data['brand'], self.product.brand)
        self.assertEqual(data['category'], self.product.category)
        self.assertEqual(float(data['rating']), self.product.rating)
        self.assertEqual(float(data['price']), self.product.price)
        self.assertEqual(data['countInStock'], self.product.countInStock)

class ReviewSerializerTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='testuser@example.com', password='password')
        self.product = Product.objects.create(user=self.user, name="Test Product")
        self.review = Review.objects.create(
            product=self.product,
            user=self.user,
            rating=5,
            comment="Great product!",
        )

    def test_review_serializer(self):
        serializer = ReviewSerializer(instance=self.review)
        data = serializer.data
        self.assertEqual(data['product'], self.product.id)
        self.assertEqual(data['user'], self.user.id)
        self.assertEqual(data['rating'], 5)
        self.assertEqual(data['comment'], "Great product!")

class OrderSerializerTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='testuser@example.com', password='password')
        self.order = Order.objects.create(
            user=self.user,
            paymentMethod="Credit Card",
            taxPrice=10.00,
            shippingPrice=5.00,
            totalPrice=115.00,
            paid=True,  # Assuming 'paid' instead of 'isPaid'
        )

    def test_order_serializer(self):
        serializer = OrderSerializer(instance=self.order)
        data = serializer.data
        self.assertEqual(data['user'], self.user.id)
        self.assertEqual(data['paymentMethod'], self.order.paymentMethod)
        self.assertEqual(float(data['taxPrice']), self.order.taxPrice)
        self.assertEqual(float(data['shippingPrice']), self.order.shippingPrice)
        self.assertEqual(float(data['totalPrice']), self.order.totalPrice)
        self.assertEqual(data['paid'], self.order.paid)

class ShippingAddressSerializerTest(TestCase):
    def setUp(self):
        self.order = Order.objects.create(
            user=User.objects.create_user(username='testuser', email='testuser@example.com', password='password')
        )
        self.address = ShippingAddress.objects.create(
            order=self.order,
            address="123 Test St",
            city="Test City",
            postalCode="12345",
            country="Test Country",
            shippingPrice=5.00,
        )

    def test_shipping_address_serializer(self):
        serializer = ShippingAddressSerializer(instance=self.address)
        data = serializer.data
        self.assertEqual(data['address'], self.address.address)
        self.assertEqual(data['city'], self.address.city)
        self.assertEqual(data['postalCode'], self.address.postalCode)
        self.assertEqual(data['country'], self.address.country)
        self.assertEqual(float(data['shippingPrice']), self.address.shippingPrice)

class OrderItemSerializerTest(TestCase):
    def setUp(self):
        self.order = Order.objects.create(
            user=User.objects.create_user(username='testuser', email='testuser@example.com', password='password')
        )
        self.product = Product.objects.create(name="Test Product")
        self.order_item = OrderItem.objects.create(
            order=self.order,
            product=self.product,
            name="Test Product",
            qty=2,
            price=50.00,
        )

    def test_order_item_serializer(self):
        serializer = OrderItemSerializer(instance=self.order_item)
        data = serializer.data
        self.assertEqual(data['name'], self.order_item.name)
        self.assertEqual(data['qty'], self.order_item.qty)
        self.assertEqual(float(data['price']), self.order_item.price)
        self.assertEqual(data['order'], self.order.id)
