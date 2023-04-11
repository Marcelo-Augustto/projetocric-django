from django.db import models

class CityManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(visible=True)