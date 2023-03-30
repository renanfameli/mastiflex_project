from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    colors = models.CharField(max_length=255)
    packaging = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name
