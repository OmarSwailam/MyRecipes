from django.conf import settings
from django.db import models


class Recipe(models.Model):
    LOW = "L"
    MEDIUM = "M"
    HIGH = "H"
    COST_CHOICES = [
        (LOW, "Low"),
        (MEDIUM, "medium"),
        (HIGH, "High"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="recipes"
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    duration = models.IntegerField()
    cost = models.CharField(max_length=1, choices=COST_CHOICES, default=LOW)
    reference_link = models.CharField(max_length=255, blank=True)
    is_public = models.BooleanField(default=False)

    tags = models.ManyToManyField("Tag", related_name="tagged_items")
    ingredients = models.ManyToManyField(
        "Ingredient", related_name="ingredient_recipes"
    )

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    KILOGRAM = "KG"
    GRAM = "G"
    REGULAR_SPOON = "RS"
    TEA_SPOON = "TS"
    LITER = "L"
    MILLILITER = "ML"
    TYPE_CHOICES = [
        (KILOGRAM, "Kilogram"),
        (GRAM, "Gram"),
        (REGULAR_SPOON, "Regular Spoon"),
        (TEA_SPOON, "Tea Spoon"),
        (LITER, "Liter"),
        (MILLILITER, "Milliliter"),
    ]

    name = models.CharField(max_length=64)
    amount = models.DecimalField(max_digits=4, decimal_places=2)
    amount_type = models.CharField(max_length=2, choices=TYPE_CHOICES, default=GRAM)
