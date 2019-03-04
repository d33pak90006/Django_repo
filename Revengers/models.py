from django.db import models
from django.contrib.auth.models import User

class suitup(models.Model):
	Name = models.CharField(max_length = 100)
	Place = models.TextField()
	friend = models.TextField()
	alias = models.TextField()
	post_user = models.ForeignKey(User,on_delete=models.CASCADE)


def __str__(self):
	self.Name = Name
