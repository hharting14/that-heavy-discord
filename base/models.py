from django.db import models
from django.contrib.auth.models import AbstractUser

from utils.models import THDModel
from utils.choices import *
import joblib


class User(THDModel, AbstractUser):
    """
    User model. Extend from Django's Abstract User, adding some extra fields:
    email, bio, and picture.
    """
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)
    avatar = models.ImageField(null=True, default="avatar.svg")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    
    def __str__(self):
        return self.username


class Topic(THDModel):
    """
    Topic model. Extend from THD Model. Each room has its associated
    topics.
    """
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Room(THDModel):
    """
    Room model. Extend from THD Model. Each room has a host, topics,
    participants, name, and some description.
    """
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)
    description = models.TextField(
        null=True,
        blank=True,
        help_text='Description of the room'
    )
    participants = models.ManyToManyField(User, related_name='participants', blank=True)

    def __str__(self):
        return self.name


class Message(THDModel):
    """
    Message model. Extend from THD Model. Users can write messages in any
    room.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.body[0:50]


class Prediction(models.Model):
    """
    Prediction model. Users can make predictions based on their choices in the form/quiz.
    """
    country = models.PositiveIntegerField(choices=COUNTRY, null=True)
    instrument = models.PositiveIntegerField(choices=INSTRUMENT, null=True)
    decade = models.PositiveIntegerField(choices=DECADE, null=True)
    mood = models.PositiveIntegerField(choices=MOOD, null=True)
    topic = models.PositiveIntegerField(choices=TOPIC, null=True)
    result = models.CharField(max_length=30, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        ml_model = joblib.load('utils/ml_bands_model.joblib')
        self.result = ml_model.predict(
            [[self.country, self.instrument, self.decade, self.mood, self.topic]])
        return super().save(*args, *kwargs)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.result
