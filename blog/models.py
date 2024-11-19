from django.db import models
#we are going to use some packages to help us
#this will help us add this model to the admin panel later
from django.conf import settings
#import functions to deal with timestamps and timezones
from django.utils import timezone

# Create your models here.

#lets make our post table

class Post(models.Model):
    #we can import information (or create a relationship/join) from other tables using the foreign key field
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #char field means a list of character with max length
    title = models.CharField(max_length=200)
    #text fields are for large amounts of text within something like a blog post
    text = models.TextField()
    #datetime deals with dates and times.. the default when a new post is made is to grab the timezone of the user and timestamp the current time
    create_date = models.DateTimeField(default=timezone.now)
    #eventually we are going to have two types of posts in our application
    #draft and published
    published_date = models.DateTimeField(blank=True, null=True)

    #a function to eventually publish our post
    def publish(self):
        self.published_date = timezone.now()
        self.save() #django way to save to a database
    
    def __str__(self):
        return self.title
