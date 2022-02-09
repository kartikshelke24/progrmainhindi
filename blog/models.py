from django.contrib.auth.models import User
from django.utils.timezone import now
from django.db import models
from taggit.managers import TaggableManager

# Create your models here.

class BlogPost(models.Model):
    sno = models.AutoField(primary_key=True)
    postTitle = models.CharField(max_length=300)
    postSlug = models.SlugField()
    postTag = TaggableManager()
    postDesc = models.TextField(blank=True)
    postContent = models.TextField()
    postImg = models.ImageField(upload_to="static/blog/blogImg/postImg")
    date_time = models.DateTimeField(blank=True)

    def __str__(self):
        return self.postTitle


class BlogComment(models.Model):
    sno = models.AutoField(primary_key=True)
    commentText = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    parent = models.ForeignKey('self',on_delete=models.CASCADE, null=True )
    timestamp =  models.DateTimeField(default=now)

    # def __str__(self):
    #     return self.user
