from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ImproperlyConfigured
from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE, PROTECT
from datetime import datetime
from django.shortcuts import reverse

class User(AbstractUser):
    pass

class categories(models.Model):
    categorie = models.CharField(max_length=22, unique=True)

    def __str__(self):
        return self.categorie  

    def get_absolute_url(self):
        return reverse("categories", kwargs={"category": self.categorie})
      

class Auction(models.Model):
    author = models.ForeignKey(User, on_delete= CASCADE, default=1)
    title = models.CharField(max_length=23)
    categorie = models.ForeignKey(categories ,on_delete=models.CASCADE, default=5)
    image = models.CharField(max_length=2048,blank=True)
    bid = models.IntegerField()
    description = models.TextField()
    isActive = models.BooleanField(default=True,blank=True)
    watchlist = models.ManyToManyField(User,blank=True,related_name="watchlist")


    def __str__(self):
        return f"{self.title} "

    def get_absolute_url(self):
        return reverse("listing_page", kwargs={"id": self.pk})

class Bids(models.Model):
    stuff = models.ForeignKey(Auction, on_delete = CASCADE)
    bidder = models.ForeignKey(User,on_delete = models.DO_NOTHING)
    time = models.DateTimeField(datetime.now())
    val = models.IntegerField()

class Comments(models.Model):
    stuff = models.ForeignKey(Auction, on_delete = CASCADE)
    author = models.ForeignKey(User, on_delete = models.DO_NOTHING)
    time = models.DateTimeField(default = datetime.now())
    text = models.TextField()

