from django.db import models


class Fields(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Fields"


class FieldOption(models.Model):
    name = models.CharField(max_length=255)
    field = models.ForeignKey(Fields, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Field Options"


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    fields = models.ManyToManyField(Fields, through='CategoryFieldValue', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class CategoryFieldValue(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    field = models.ForeignKey(Fields, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Category Field Values"


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Products"


class ProductFieldValue(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    field = models.ForeignKey(Fields, on_delete=models.CASCADE)
    option = models.ForeignKey(FieldOption, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Product Field Values"
