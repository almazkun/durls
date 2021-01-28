# Generated by Django 3.1.5 on 2021-01-28 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("durls", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="destination",
            name="destination_url",
            field=models.URLField(max_length=255, verbose_name="Destination URL"),
        ),
        migrations.AlterField(
            model_name="destination",
            name="slug",
            field=models.SlugField(
                allow_unicode=True,
                max_length=255,
                unique=True,
                verbose_name="Path for short URL",
            ),
        ),
    ]
