from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class Neighborhood(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    description = models.TextField()
    health_tell = models.IntegerField(null=True, blank=True)
    police_number = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    def save_neighborhood(self):
        self.save()
    def delete_neighborhood(self):
        self.delete()
    @classmethod
    def find_neighborhood(cls,name):
        return cls.objects.filter(name__icontains=name)
    @classmethod
    def update_neighborhood(cls,id,name):
        return cls.objects.filter(id=id).update(name=name)
        
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile') 
    name = models.CharField(max_length=50)
    bio=models.TextField()
    profile_picture = models.ImageField(upload_to='images/', default='default.png')
    neighborhood=models.ForeignKey(Neighborhood,on_delete=models.SET_NULL,null=True,related_name='neighbors',blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def save_profile(self):
        self.user

    def delete_profile(self):
        self.delete()

    @classmethod
    def search_profile(cls, search_term):
        return cls.objects.filter(user__username__icontains=search_term).all()
    def __str__(self):
        return f'{self.user.username} Profile'

class Business(models.Model):
    business_name=models.CharField(max_length=50)
    description = models.TextField(blank=True)
    email =models.EmailField()
    user=models.ForeignKey(Profile,on_delete=models.CASCADE) 
    neighborhood = models.ForeignKey(Neighborhood,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def save_business(self):
        self.save()
    def delete_business(self):
        self.delete()
    @classmethod
    def find_business(cls,name):
        return cls.objects.filter(name__icontains=name)

    @classmethod
    def update_business(cls,id,name):
        update = cls.objects.filter(id=id).update(name=name)
        return update 
class Post(models.Model):
    title = models.CharField(max_length=120, null=True)
    post = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='post_owner')
    hood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, related_name='hood_post')

    def __str__(self):
        return self.title
