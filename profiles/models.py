from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField


# Edited from source: Code Institute Boutique Ado
class UserProfile(models.Model):
    """
    A user profile model for maintaining default
    address information, order history and emergency contact info
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)
    default_country = CountryField(blank_label='Country *', null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_town_or_city = models.CharField(max_length=40, null=True, blank=True)
    default_street_address1 = models.CharField(max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(max_length=80, null=True, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)
    deafult_emergency_contact = models.CharField(
        max_length=50, null=True, blank=True)
    default_emergency_number = PhoneNumberField(null=True, blank=True)
    default_medical = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.username


# Source: Code Institute Boutique Ado
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()