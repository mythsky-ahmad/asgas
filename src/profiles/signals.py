from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile , Relationship

# to create profile to the user
@receiver(post_save , sender=User)
def post_save_create_profile(sender , instance, created , **kwargs):
    if created:
        Profile.objects.create(user=instance)


# friends list inserting automaticly
@receiver(post_save , sender=Relationship )
def post_save_add_to_friends(sender , instance , created , **kwargs):
    friend_request_sender = instance.sender
    friend_request_receiver = instance.receiver

    if instance.status == "accepted":
        friend_request_sender.friends.add(friend_request_receiver.user)
        friend_request_receiver.friends.add(friend_request_sender.user)

        friend_request_sender.save()
        friend_request_receiver.save()