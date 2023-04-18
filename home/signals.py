from .models import CityManager
from cities.models import City

from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=City)
def update_city_manager(sender, instance, created, **kwargs):
    if instance.visible:
        # Atualiza ou cria uma nova instância de CityManager para a cidade visível
        CityManager.objects.update_or_create(city=instance)
    else:
        # Se a cidade não for mais visível, exclua a instância correspondente de CityManager (se houver)
        CityManager.objects.filter(city=instance).delete()
