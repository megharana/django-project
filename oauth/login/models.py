from django.db import models

class User(models.Model):
	username = models.CharField(max_length=30)
	usertype = models.CharField(max_length=10)
	userAvatarUrl = models.URLField(default="")
	createdDate = models.CharField(max_length=10,default="")

	def __str__(self):
		return self.username