from django.db import models
from django.conf import settings


class TourCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tour(models.Model):
    category = models.ForeignKey(TourCategory, related_name='tours', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='tour_photos/', blank=True, null=True)
    description = models.TextField()
    location = models.CharField(max_length=255)  # Поле для локации

    def __str__(self):
        return self.name


class Review(models.Model):
    tour = models.ForeignKey(Tour, related_name='reviews', on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Review by {self.author} on {self.tour}'
    

class TourBook(models.Model):
    tour = models.ForeignKey(Tour, related_name='books', on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    commentary = models.TextField()
    number_of_people = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Inquiry for {self.tour.name} by {self.phone_number}"