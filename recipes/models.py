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
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user"
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    duration = models.IntegerField()
    cost = models.CharField(max_length=1, choices=COST_CHOICES, default=LOW)
    reference_link = models.CharField(max_length=255, blank=True)
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return self.title
