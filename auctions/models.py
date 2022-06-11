from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    pass

class Listing(models.Model):
    title = models.CharField(max_length=60)
    flActive = models.BooleanField(default=True)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.CharField(null=True, max_length=300)
    startingBid = models.FloatField()
    currentBid = models.FloatField(blank=True, null=True)
    creator = models.ForeignKey(User, on_delete=models.PROTECT, related_name="all_creators_listings")
    watchers = models.ManyToManyField(User, blank=True, related_name="watched_listings")
    buyer = models.ForeignKey(User, null=True, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.title} - {self.startingBid}"

class Picture(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="get_pictures")
    picture = models.ImageField(upload_to="images/")
    alt_text = models.CharField(max_length=140)
