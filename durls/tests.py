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
        self.assertTemplateUsed(response, "durls/destination_list.html")

    def test_add_delete_view(self):
        self.client.post(reverse("create"), self.dest_data)
        dest = Destination.objects.get(slug=self.dest_data["slug"])

        self.assertEqual(dest.slug, self.dest_data["slug"])
        self.assertEqual(dest.destination_url, self.dest_data["destination_url"])
        self.assertEqual(dest.visits, 0)

        self.client.post(reverse("delete", args=[self.dest_data["slug"]]))
        with self.assertRaises(Destination.DoesNotExist):
            Destination.objects.get(slug=self.dest_data["slug"])

    def test_redirect_view(self):
        self.client.post(reverse("create"), self.dest_data)
        response = self.client.get(reverse("redirect", args=[self.dest_data["slug"]]))
        dest = Destination.objects.get(slug=self.dest_data["slug"])

        self.assertEqual(response.status_code, 301)
        self.assertEqual(response.url, self.dest_data["destination_url"])
        self.assertEqual(dest.visits, 1)
        self.assertEqual(f"{dest}", self.dest_data["slug"])

    def test_get_not_allowed(self):
        response = self.client.get(reverse("create"))
        self.assertEqual(response.status_code, 301)
        response = self.client.get(reverse("delete", args=[self.dest_data["slug"]]))
        self.assertEqual(response.status_code, 301)

