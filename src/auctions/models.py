from django.db import models
from signups.models import User


# Create your models here.
class Article(models.Model):
    link = models.CharField(max_length=2083)
    title = models.CharField(max_length=2000)
    author = models.ForeignKey(User)
    published_on = models.DateTimeField(auto_now_add=True)
    
class Bidding(models.Model):
    article = models.ForeignKey(Article)
    bidder = models.ForeignKey(User)
    bid_price = models.DecimalField(max_digits=10, decimal_places=2)
    win = models.BooleanField()
    created_on = models.DateTimeField(auto_now_add=True)