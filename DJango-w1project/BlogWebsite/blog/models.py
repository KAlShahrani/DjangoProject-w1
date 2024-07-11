from django.contrib.auth.hashers import make_password
from django.db import models

class User(models.Model):
    uid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.password = make_password(self.password)
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.uid} {self.username}"

class Post(models.Model):
    pid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField(null=False)
    category = models.CharField(null=True, max_length=255)
    date_published = models.DateField(null=True)

    def __str__(self):
        return f"{self.title} - {self.category}"

class Comment(models.Model):
    cid = models.AutoField(primary_key=True)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(null=False, max_length=500)
    date_posted = models.DateField(null=True)

    def __str__(self):
        return f"{self.content} - {self.post_id}"

class Category(models.Model):
    caid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"{self.name}"
