" " " building models  " " "
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils.text import slugify
from cloudinary.models import CloudinaryField

from django.db.models.signals import post_save
from django.utils.text import slugify




STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    '''model for creating a Post'''
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)

class Profile(models.Model):
    '''model for creating a Post'''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=80, null=True, blank=True)
    location = models.CharField(max_length=80, null=True, blank=True)
    url = models.CharField(max_length=80, null=True, blank=True)
    profile_info = models.TextField(max_length=200, null=True, blank=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    created = models.DateField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)




#     class Meta:
#         """
#         newer posts will be shown
#         in decending order based on when
#         they were created

#         """
#         ordering = ['-created_on']

#     def __str__(self):
#         return self.title

#     def number_of_likes(self):
#         ''' count the number of likes a post has recieved '''
#         return self.likes.count()


# class Comment(models.Model):
#     ''' creating a model for comments '''
#     post = models.ForeignKey(Post, on_delete=models.CASCADE,
#                              related_name='comments')
#     name = models.CharField(max_length=80)
#     email = models.EmailField()
#     body = models.TextField()
#     created_on = models.DateTimeField(auto_now_add=True)
#     approved = models.BooleanField(default=False)

#     class Meta:
#         """
#         comments will be shown
#         in order based on when
#         they were created oldest
#         comments listed first

#         """
#         ordering = ['created_on']

#     def __str__(self):
#         return f"Comment {self.body} by {self.name}"


# def user_directory_path(instance, filename):
#     ''' file will be uploded to media root/ user(ID)/filename '''
#     return 'user {0}/{1}'.format(instance.user.id, filename)