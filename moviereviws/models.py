from django.db import models

# Create your models here.
class Movies(models.Model):
    # ID = models.AutoField
    Title = models.CharField(max_length=50)
    Description = models.TextField()
    def __str__(self):
        return self.Title

class Review(models.Model):
    # ID = models.AutoField
    MovieID = models.ForeignKey(Movies, on_delete=models.CASCADE)
    Username = models.CharField(max_length=50)
    ReviewTitle = models.CharField(max_length=50)
    ReviewContent = models.TextField()
    def __str__(self):
        return self.ReviewTitle