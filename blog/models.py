from django.db import models
from django.utils import timezone


class Post(models.Model):
    #defining the properties:

    #link to another model
    author = models.ForeignKey('auth.User')

    #how you define text test w/ limited characters
    title = models.CharField(max_length=200)

    #how you define text w/ no limit to characters
    text = models.TextField()

    #date/time
    created_date = models.DateTimeField(
            default=timezone.now)


    published_date = models.DateTimeField(
            blank=True, null=True)

    #function for publishing
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
