from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from api.models import Product, Review

class ProductViewTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        self.product_1 = Product.objects.create(
            name="Product 1",
            brand="Brand A",
            category="Category A",
            description="Description 1",
            rating=4.5,
            numReviews=2,
            price=50.00,
            countInStock=10
        )

        self.product_2 = Product.objects.create(
            name="Product 2",
            brand="Brand B",
            category="Category B",
            description="Description 2",
            rating=3.5,
            numReviews=1,
            price=30.00,
            countInStock=5
        )

        self.product_3 = Product.objects.create(
            name="Product 3",
            brand="Brand C",
            category="Category C",
            description="Description 3",
            rating=5.0,
            numReviews=3,
            price=70.00,
            countInStock=2
        )

    def test_get_products(self):
        url = reverse('get-products')
        response = self.client.get(url, {'keyword': 'Product'})


        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['products']), 3)

    def test_get_top_products(self):
        url = reverse('get-top-products')
        response = self.client.get(url)


        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_get_product(self):
        url = reverse('get-product', kwargs={'pk': self.product_1.id})
        response = self.client.get(url)


        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Product 1')

    def test_create_product_review_authenticated(self):
        self.client.login(username='testuser', password='testpassword')
        url = reverse('create-product-review', kwargs={'pk': self.product_1.id})
        data = {
            'rating': 5,
            'comment': 'Excellent product!'
        }
        response = self.client.post(url, data, format='json')


        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('Revisão adicionada', response.data)

    def test_create_product_review_already_exists(self):
        self.client.login(username='testuser', password='testpassword')
        Review.objects.create(
            user=self.user,
            product=self.product_1,
            name=self.user.first_name,
            rating=4,
            comment="Good product"
        )

        url = reverse('create-product-review', kwargs={'pk': self.product_1.id})
        data = {
            'rating': 5,
            'comment': 'Excellent product!'
        }
        response = self.client.post(url, data, format='json')


        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('Produto já revisado', response.data)

    def test_create_product_review_invalid_rating(self):
        self.client.login(username='testuser', password='testpassword')
        url = reverse('create-product-review', kwargs={'pk': self.product_1.id})
        data = {
            'rating': 0,
            'comment': 'Not good!'
        }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('Selecione uma classificação', response.data)

