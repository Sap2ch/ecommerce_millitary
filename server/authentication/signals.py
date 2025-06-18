from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from users.models import Profile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
            # phone_number=instance['phone_number'],
            # state=instance['state'],
            # status=instance['status']
        # )

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

@receiver(pre_save, sender=User)
def set_username_lowercase(sender, instance, **kwargs):
    """
        ЗБЕРЕЖЕННЯ ЮЗЕРНЕЙМУ В НИЖНЬОМУ РЕГІСТРІ
    """
    if instance.username:  
        instance.username = instance.username.lower()