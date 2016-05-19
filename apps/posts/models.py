from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    post = models.TextField(max_length=300)
    created_at = models.DateField()
    user = models.ForeignKey(User)
    reciever = models.ForeignKey(User, related_name='reciever')
    def __str__(self):
        return self.user.first_name
    class Meta:
        db_table='posts'
class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    comment = models.TextField(max_length=300)
    created_at = models.DateField()
    post = models.ForeignKey(Post)
    user = models.ForeignKey(User)
    def __str__(self):
        return self.user.first_name
    class Meta:
        db_table='comments'
