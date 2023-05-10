from django.db import models
from django.contrib.auth.models import User

class Deck(models.Model):
    title = models.CharField(max_length=50)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
class Card(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    back = models.CharField(max_length=250)
    date_created = models.DateTimeField(auto_now_add=True)
    learned = models.BooleanField(default=False)
    deck = models.ForeignKey("Deck", on_delete=models.CASCADE)
    number_of_practice_needed = models.IntegerField(default=5, editable=False)

    def __str__(self) -> str:
        return self.title
