from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# class User(models.Model):
#     id = models.AutoField(primary_key=True)
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     password = models.CharField(max_length=10)
#     def __str__(self):
#         return self.ip
#     class Meta:
#         db_table = 'users'
class UserProfile(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField(max_length=300)
    user = models.OneToOneField(User)
    def __str__(self):
        return self.user.first_name
    class Meta:
        db_table='users'
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile, created = UserProfile.objects.get_or_create(user=instance)
post_save.connect(create_user_profile, sender=User)
