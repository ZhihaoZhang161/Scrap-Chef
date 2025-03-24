from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    Occupation = models.CharField(max_length=100, blank=True, null=True)
    Profile_photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)

    def __str__(self):
        return self.User.username
    
class Post(models.Model):
    Media = models.ImageField(upload_to='posts_photos/')
    Caption = models.CharField(max_length=255)
    Date = models.DateTimeField(auto_now_add=True)
    User = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.Caption
    
class Review(models.Model):
    Taste = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])  
    Struggle = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])  
    Preparation = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    Post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f"Review {self.id}"
    
class List(models.Model):
    Title = models.CharField(max_length=64)
    Description = models.TextField()
    PostID = models.CharField(max_length=64)

    def __str__(self):
        return self.Title