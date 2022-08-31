from django.test import TestCase
from django.urls import reverse


# Тесты для главной страницы
class IndexPageTestCase(TestCase):
    def test_correct_template_on_index_page(self):
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'index.html')