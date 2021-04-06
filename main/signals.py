from django.contrib.auth.models import User
from main.models import Profile
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()



@receiver(post_delete, sender=Profile)
def auto_delete_user(sender, instance, **kwargs):
	if instance.user:
		instance.user.delete()