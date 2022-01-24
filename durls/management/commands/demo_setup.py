from django.conf import settings
from django.core.management.base import BaseCommand

from accounts.models import CustomUser
from durls.models import Destination


class Command(BaseCommand):
    help = "Populates DB with demo data"

    def handle(self, *args, **options):
        password = settings.DURLS_DEMO_PASSWORD
        demo_admin_email = settings.DURLS_DEMO_ADMIN_EMAIL
        demo_user_email = settings.DURLS_DEMO_USER_EMAIL
        destination_slug = "go"

        if not CustomUser.objects.filter(email=demo_admin_email).exists():
            CustomUser.objects.create_superuser(email=demo_admin_email, password=password)
            self.stdout.write(f"Admin Created: {demo_admin_email}")

        if not CustomUser.objects.filter(email=demo_user_email).exists():
            CustomUser.objects.create_user(email=demo_user_email, password=password)
            self.stdout.write(f"User Created: {demo_user_email}")

        if not Destination.objects.filter(slug=destination_slug).exists():
            Destination.objects.create(
                owner=CustomUser.objects.get(email=demo_user_email),
                slug=destination_slug,
                destination_url="https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=bilgogi",
            )
            self.stdout.write(f"Destination Created: {destination_slug}")

        self.stdout.write(
            self.style.SUCCESS("Successfully populated DB with demo data")
        )
