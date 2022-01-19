from django.test import TestCase, Client
from django.urls import reverse
from durls.models import Destination
from accounts.models import CustomUser
from durls.seervices import destination_all, destination_for_user

# Create your tests here.
class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.dest_data = {
            "slug": "go",
            "destination_url": "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=bilgogi",
        }
        self.user_signup_data = {
            "email": "some@email.com",
            "password1": "some_password",
            "password2": "some_password",
        }
        self.user_login_data = {
            "email": self.user_signup_data["email"],
            "password": self.user_signup_data["password1"],
        }

    def test_home_view(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "durls/home.html")

    def test_manage_view(self):
        c = self.client
        response = c.get(reverse("create"))

        self.assertEqual(response.status_code, 302)

        c.post(reverse("signup"), self.user_signup_data)
        c.login(
            email=self.user_login_data["email"],
            password=self.user_login_data["password"],
        )
        response = c.get(reverse("create"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "durls/destination_list.html")

    def test_add_delete_view(self):
        c = self.client
        c.post(reverse("signup"), self.user_signup_data)
        c.login(
            email=self.user_login_data["email"],
            password=self.user_login_data["password"],
        )
        c.post(reverse("create"), self.dest_data)
        dest = Destination.objects.get(slug=self.dest_data["slug"])

        self.assertEqual(dest.slug, self.dest_data["slug"])
        self.assertEqual(dest.destination_url, self.dest_data["destination_url"])
        self.assertEqual(dest.visits, 0)

        c1 = self.client
        another_user_data = self.user_signup_data.copy()
        another_user_data.update({"email": "another@email.com"})
        c1.post(reverse("signup"), another_user_data)
        c1.login(
            email=another_user_data["email"], password=another_user_data["password1"]
        )

        response = self.client.post(reverse("delete", args=[self.dest_data["slug"]]))
        self.assertEqual(response.status_code, 404)

        c.login(
            email=self.user_login_data["email"],
            password=self.user_login_data["password"],
        )
        self.client.post(reverse("delete", args=[self.dest_data["slug"]]))
        with self.assertRaises(Destination.DoesNotExist):
            Destination.objects.get(slug=self.dest_data["slug"])

    def test_redirect_view(self):
        c = self.client
        c.post(reverse("signup"), self.user_signup_data)
        c.login(
            email=self.user_login_data["email"],
            password=self.user_login_data["password"],
        )
        c.post(reverse("create"), self.dest_data)

        response = self.client.get(reverse("redirect", args=[self.dest_data["slug"]]))
        dest = Destination.objects.get(slug=self.dest_data["slug"])

        self.assertEqual(response.status_code, 301)
        self.assertEqual(response.url, self.dest_data["destination_url"])
        self.assertEqual(dest.visits, 1)
        self.assertEqual(f"{dest}", self.dest_data["slug"])


class TestServices(TestCase):
    def setUp(self):
        self.user_one = CustomUser.objects.create_user(email="some@email.com")
        self.user_two = CustomUser.objects.create_user(email="some_other@email.com")
        self.dest_one = Destination.objects.create(
            owner=self.user_one, slug="one", destination_url="https://www.google.com"
        )
        self.dest_two = Destination.objects.create(
            owner=self.user_two, slug="two", destination_url="https://www.google.co.kr"
        )

    def test_destination_all(self):
        dest_all = destination_all()
        self.assertEqual(dest_all.count(), Destination.objects.all().count())

    def test_destination_for_user_one(self):
        dest_for_user = destination_for_user(self.user_one)
        self.assertEqual(
            dest_for_user.count(),
            Destination.objects.filter(owner=self.user_one).count(),
        )
        self.assertTrue(self.dest_one in dest_for_user)

    def test_destination_for_user_two(self):
        dest_for_user = destination_for_user(self.user_two)
        self.assertEqual(
            dest_for_user.count(),
            Destination.objects.filter(owner=self.user_two).count(),
        )
        self.assertTrue(self.dest_two in dest_for_user)
