from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    profile_pic=models.ImageField(upload_to="profilepics",null=True,blank=True)
    bio=models.CharField(max_length=200,null=True)
    address=models.CharField(max_length=200,null=True)
    dob=models.DateTimeField(null=True)
    following=models.ManyToManyField("self",related_name="followed_by",symmetrical=False)
    created_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    
class Posts(models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to="postimages",null=True,blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="userposts")
    created_date=models.DateTimeField(auto_now_add=True)
    liked_by=models.ManyToManyField(User,related_name="post_like")

    def __str__(self):
        return self.title

class Comments(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="comment")
    comment_text=models.CharField(max_length=200)
    post=models.ForeignKey(Posts,on_delete=models.CASCADE,related_name="post_comment")
    created_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_text


def create_profile(sender,instance,created,**kwargs):
    if created:
        UserProfile.objects.create(user=instance)


post_save.connect(create_profile,sender=User)        