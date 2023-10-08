from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.
class WatchList(models.Model):
    title=models.CharField(max_length=40)
    category=models.CharField(max_length=30)
    storyline=models.CharField(max_length=200)
    avg_rating=models.FloatField(default=0)
    number_ratings=models.PositiveIntegerField(default=0)
    active=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.title
    
class Review(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    watchlist=models.ForeignKey(WatchList,on_delete=models.CASCADE,related_name='reviews')
    rating=models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    description=models.CharField(max_length=200)
    active=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.rating)+' || '+self.watchlist.title
    


    