from django.contrib.auth.models import User
from .models import HospitalUser
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwards):
	if created:
		HospitalUser.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwards):
	instance.admins.save()
