from rest_framework.test import APITestCase
import rest_framework.status as status
from django.urls import reverse_lazy


class HydraTestCase(APITestCase):


    def test_index_page_get(self):
        url = reverse_lazy('homepage')
        code = self.client.get(url).status_code
        self.assertEqual(status.HTTP_200_OK, code)

    def test_logout_page_get(self):
        url = reverse_lazy('logout')
        code = self.client.get(url).status_code
        self.assertEqual(status.HTTP_302_FOUND, code)

    def test_login_page_get(self):
        url = reverse_lazy('login')
        code = self.client.get(url).status_code
        self.assertEqual(status.HTTP_200_OK, code)

    def test_regist_page_get(self):
        url = reverse_lazy('register')
        code = self.client.get(url).status_code
        self.assertEqual(status.HTTP_200_OK, code)

    def test_prodlist_page_get(self):
        url = reverse_lazy('product_list')
        code = self.client.get(url).status_code
        self.assertEqual(status.HTTP_200_OK, code)

    def test_categ_page_get(self):
        url = reverse_lazy('categories')
        code = self.client.get(url).status_code
        self.assertEqual(status.HTTP_200_OK, code)

    def test_concrs_page_get(self):
        url = reverse_lazy('concrete_category')
        code = self.client.get(url).status_code
        self.assertEqual(status.HTTP_200_OK, code)
    def test_concrs_page_get(self):
40
        url = reverse_lazy('concrete_category')
41
        code = self.client.get(url).status_code
42
        self.assertEqual(status.HTTP_200_OK, code)
43
​
44
    def test_prod_detail_page_get(self):
45
        url = reverse_lazy('product_detail', args=(1,))
46
        code = self.client.get(url).status_code
47
        self.assertEqual(status.HTTP_200_OK, code)
48
​
49
    def test_cart_add_page_get(self):
50
        url = reverse_lazy('cart_add')
51
        code = self.client.get(url).status_code
52
        self.assertEqual(status.HTTP_200_OK, code)
    def test_prod_detail_page_get(self):
        url = reverse_lazy('product_detail', args=(1,))
        code = self.client.get(url).status_code
        self.assertEqual(status.HTTP_200_OK, code)

    def test_cart_add_page_get(self):
        url = reverse_lazy('cart_add')
        code = self.client.get(url).status_code
        self.assertEqual(status.HTTP_200_OK, code)

    def test_create_product_page_get(self):
        url = reverse_lazy('create_product')
        code = self.client.get(url).status_code
        self.assertEqual(status.HTTP_200_OK, code)

    def test_create_cat_page_get(self):
        url = reverse_lazy('create_category')
        code = self.client.get(url).status_code
        self.assertEqual(status.HTTP_200_OK, code)

    def test_index_page_get(self):
        url = reverse_lazy('update_product', args=(1,))
        code = self.client.get(url).status_code
        self.assertEqual(status.HTTP_200_OK, code)
