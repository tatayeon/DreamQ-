# Generated by Django 5.0.4 on 2024-05-11 23:21

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Attraction",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=30)),
                ("type", models.CharField(max_length=30)),
                ("content", models.TextField()),
                (
                    "head_image",
                    models.ImageField(blank=True, upload_to="blog/images/%Y/%m/%d/"),
                ),
                ("Limit", models.TextField()),
            ],
        ),
    ]