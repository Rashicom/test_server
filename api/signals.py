from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import room_teachers


@receiver(post_save, sender=room_teachers)
def save_teacher(sender, instance, created, **kwargs):
    print("signal filred")


    