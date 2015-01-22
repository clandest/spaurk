from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    text = models.TextField()

class Artist(models.Model):
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    twitter = models.CharField(max_length=50)
    facebook = models.CharField(max_length=50)
    youtube = models.CharField(max_length=50)
    website = models.CharField(max_length=50)
    dateTime = models.DateTimeField()

    def __str__(self):
        return self.name

class Song(models.Model):
    artist = models.ForeignKey(Artist)
    title = models.CharField(max_length=30)
    sample = models.CharField(max_length=50)
    spaurkCount = models.IntegerField(default=0)
    dateTime = models.DateTimeField()

    def __str__(self):
        return self.title
