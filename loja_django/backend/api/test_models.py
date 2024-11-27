from django.test import TestCase
from django.contrib.auth.models import User
from api.models import Product, Review, Order, OrderItem, ShippingAddress


class TestModels(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.product = Product.objects.create(
            user=self.user,
            name="Test Product",
            brand="Test Brand",
            price=99.99,
            countInStock=10,
        )
        self.order = Order.objects.create(
            user=self.user,
            paymentMethod="Credit Card",
            taxPrice=5.00,
            shippingPrice=2.50,
            totalPrice=107.49,
            isPaid=True,
        )
        self.order_item = OrderItem.objects.create(
            product=self.product,
            order=self.order,
            name="Test Product",
            qty=2,
            price=99.99,
        )
        self.shipping_address = ShippingAddress.objects.create(
            order=self.order,
            address="123 Test Street",
            city="Test City",
            postalCode="12345",
            country="Test Country",
            shippingPrice=10.00,
        )
        self.review = Review.objects.create(
            product=self.product,
            user=self.user,
            name="Test Review",
            rating=4,
            comment="Great product!",
        )

    def test_product_creation(self):
        self.assertEqual(self.product.name, "Test Product")
        self.assertEqual(self.product.price, 99.99)

    def test_review_creation(self):
        self.assertEqual(self.review.rating, 4)
        self.assertEqual(self.review.comment, "Great product!")

    def test_order_creation(self):
        self.assertEqual(self.order.totalPrice, 107.49)
        self.assertTrue(self.order.isPaid)

    def test_order_item_creation(self):
        self.assertEqual(self.order_item.qty, 2)
        self.assertEqual(self.order_item.price, 99.99)

    def test_shipping_address_creation(self):
        self.assertEqual(self.shipping_address.address, "123 Test Street")
        self.assertEqual(self.shipping_address.city, "Test City")
