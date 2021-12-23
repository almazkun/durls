from django.test import TestCase, Client
from django.urls import reverse
from durls.models import Destination


# Create your tests here.
class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.dest_data = {
            "slug": "go",
            "destination_url": "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=bilgogi",
        }

    def test_home_view(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "durls/home.html")

    def test_manage_view(self):
        response = self.client.get(reverse("manage"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "destination_list.html")

    def test_redirect_view(self):
        dest = Destination(**self.dest_data)
        dest.save()
        response = self.client.get(self.dest_data["slug"])

        self.assertEqual(response.status_code, 301)
        self.assertEqual(response.url, self.dest_data["destination_url"])
