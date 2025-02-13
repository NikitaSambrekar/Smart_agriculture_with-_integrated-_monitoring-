from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

class Consumer(models.Model):
    name = models.CharField(max_length=100, verbose_name="Scheme Name")
    email = models.EmailField(max_length=277, verbose_name="Scheme URL")
    image = models.ImageField(upload_to='consumer_images/', null=True, blank=True, verbose_name="Consumer Image")
    content = models.TextField(verbose_name="Scheme Discription", blank=True, null=True)

    def __str__(self):
        return str(self.id)

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name


class Review(models.Model):
    consumer = models.ForeignKey(Consumer, on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    def __str__(self):
        return f'Review for {self.consumer.name}'

# 101224
from django.db import models

class PlantDisease(models.Model):
    disease_name = models.CharField(max_length=100)
    type_of_disease = models.CharField(max_length=100)
    natural_fertilizer = models.TextField()
    suggestion = models.TextField()
    recommendation = models.TextField()

    def __str__(self):
        return self.disease_name

from django.db import models
from django.utils.timezone import now

class ImagePrediction(models.Model):
    image_name = models.CharField(max_length=255)
    image_hash = models.CharField(max_length=64, unique=True)  # Assuming SHA-256 hash
    prediction = models.CharField(max_length=255)
    detection_info = models.TextField()
    fertilizer = models.TextField(null=True)  # Add this field for the fertilizer info
    suggestion = models.TextField()
    recommendation = models.TextField()
    uploaded_at = models.DateTimeField(default=now)
    image = models.ImageField(upload_to='uploaded_images/',null=True)  # Add the image field

    def __str__(self):
        return self.image_name
