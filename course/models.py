from tkinter.tix import Balloon
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from taggit.managers import TaggableManager


# Create your models here.

class Course(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500)
    slug = models.SlugField(max_length=200)
    postTag = TaggableManager()
    desc = models.TextField()
    image = models.ImageField(upload_to="static/img/videosLogo")
    date_time = models.DateTimeField(auto_now_add=True,blank=True) 

    def __str__(self):
        return self.title
    

class Playlist(models.Model):
    sno = models.AutoField(primary_key=True)
    courseTitle = models.ForeignKey("course.Course",on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=500)
    video = models.CharField(max_length=500)
    slug = models.SlugField(max_length=200)
    contentDesc = models.TextField(blank=True)
    content = models.TextField()
    tags = TaggableManager()
    date_time = models.DateTimeField(auto_now_add=True,blank=True)  

    def __str__(self):
        return self.title




class CourseComment(models.Model):
    sno = models.AutoField(primary_key=True)
    commentText = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    parent = models.ForeignKey('self',on_delete=models.CASCADE, null=True )
    timestamp =  models.DateTimeField(default=now)