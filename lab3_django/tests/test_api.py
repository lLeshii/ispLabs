from rest_framework.test import APITestCase
import rest_framework.status as status
from django.urls import reverse_lazy

class HydraTestCase(APITestCase):
    def test_index_page_get(self):
        url = reverse_lazy('index')
        code = self.client.get(url).status_code
        self.assertEqual(status.HTTP_200_OK, code)