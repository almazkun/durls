from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _
from django.utils.text import slugify

# Create your models here.
class Destination(models.Model):
    slug = models.SlugField(_("Path for short URL"), unique=True, allow_unicode=True, max_length=255)
    destination_url = models.URLField(_("Destination URL"), max_length=255)
    visits = models.IntegerField(_("Number of visits"), default=0)

    created_on = models.DateTimeField(_("Created on"), auto_now_add=True)
    updated_on = models.DateTimeField(_("Updated on"), auto_now=True)

    class Meta:
        verbose_name = _("Destination")
        verbose_name_plural = _("Destinations")
        ordering = ["-created_on"]

    def __str__(self):
        return self.slug
    
    def add_visit(self, number=1):
        self.visits += number
        self.save()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.slug, allow_unicode=True)
        super().save(*args, **kwargs)
