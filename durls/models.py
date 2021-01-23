from django.db import models
from django.urls import reverse
from django.utils.translation import get_text as _

# Create your models here.
class Destination(models.Model):
    slug = models.SlugField(_("Path for short URL"), unique=True)
    destination_url = models.URLField(_("Destination URL"), max_length=200)
    visits = models.IntegerField(_("Number of visits"), default=0)

    created_on = models.DateTimeField(_("Created on"), auto_now_add=True)
    updated_on = models.DateTimeField(_("Updated on"), auto_now=True)

    class Meta:
        verbose_name = _("Destination")
        verbose_name_plural = _("Destinations")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Destination_detail", kwargs={"pk": self.pk})
