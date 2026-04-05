from django.db import models

class Destination(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    price_inr = models.IntegerField()
    category = models.CharField(max_length=50, choices=[('Influencer Famous', 'Influencer Famous'), ('Untouched Offbeat', 'Untouched Offbeat')])
    image_url = models.URLField(max_length=500)
    is_luxury = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Review(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100)
    comment = models.TextField()
    rating = models.IntegerField(default=5)

    def __str__(self):
        return f"{self.user_name} - {self.destination.name}"