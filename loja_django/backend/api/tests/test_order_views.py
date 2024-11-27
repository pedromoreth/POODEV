from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from api.models import Order, Product

class OrderViewsTests(APITestCase):
    def setUp(self):

        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

        self.product = Product.objects.create(name='Test Product', price=100.00)


        self.order = Order.objects.create(user=self.user, total_price=200.00)

        self.order_item = self.order.orderitem_set.create(
            product=self.product,
            quantity=2,
            price=100.00
        )

    def test_add_order_items(self):
        url = reverse('orders-add')
        data = {
            'product': self.product.id,
            'quantity': 3,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['product'], self.product.id)
        self.assertEqual(response.data['quantity'], 3)

    def test_get_my_orders(self):
        url = reverse('myorders')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)

    def test_get_order_by_id(self):
        url = reverse('user-order', args=[str(self.order.id)])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], self.order.id)

    def test_update_order_to_paid(self):
        url = reverse('pay', args=[str(self.order.id)])
        data = {'paid': True}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['paid'], True)
