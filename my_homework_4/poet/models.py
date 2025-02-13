from django.db import models
import random


class Poet(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    poetry = models.TextField(max_length=100)  # Лучше использовать TextField для хранения длинных стихов

