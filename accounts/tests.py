from django.test import TestCase
from accounts.models import CustomUser
from django.db.utils import IntegrityError

# Create your tests here.
class TestModels(TestCase):
    def setUp(self):
        self.user_data = {
            "email": "some@email.com",
            "password": "some_password",
        }
        self.admin_data = {
            "email": "admin@email.com",
            "password": "admin_password",
        }

    def test_custom_user(self):
        user = CustomUser.objects.create_user(**self.user_data)

        self.assertEqual(user.email, self.user_data["email"])
        self.assertTrue(user.check_password(self.user_data["password"]))

    def test_custom_user_admin(self):
        admin = CustomUser.objects.create_superuser(**self.admin_data)

        self.assertEqual(admin.email, self.admin_data["email"])
        self.assertTrue(admin.check_password(self.admin_data["password"]))
        self.assertTrue(admin.is_staff)
        self.assertTrue(admin.is_superuser)

    def test_custom_user_str(self):
        user = CustomUser.objects.create_user(**self.user_data)
        admin = CustomUser.objects.create_superuser(**self.admin_data)

        self.assertEqual(str(user), self.user_data["email"])
        self.assertEqual(str(admin), self.admin_data["email"])

    def test_custom_user_raises(self):
        user = CustomUser.objects.create_user(**self.user_data)

        no_email_user = self.user_data.copy()
        no_email_user["email"] = ""

        staff = self.admin_data.copy()
        staff["is_staff"] = False

        admin = self.admin_data.copy()
        admin["is_superuser"] = False

        with self.assertRaises(IntegrityError):
            CustomUser.objects.create_user(**self.user_data)
        with self.assertRaises(ValueError):
            CustomUser.objects.create_user(**no_email_user)
        with self.assertRaises(ValueError):
            CustomUser.objects.create_superuser(**staff)
        with self.assertRaises(ValueError):
            CustomUser.objects.create_superuser(**admin)
