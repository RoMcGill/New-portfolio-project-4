" " " building models  " " "
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    '''model for creating a Post'''
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="posts")
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)

    class Meta:
        """
        newer posts will be shown
        in decending order based on when
        they were created

        """
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        ''' count the number of likes a post has recieved '''
        return self.likes.count()


class Comment(models.Model):
    ''' creating a model for comments '''
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        """
        comments will be shown
        in order based on when
        they were created oldest
        comments listed first

        """
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
