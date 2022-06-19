from django.db import models
from django.contrib.auth.models import User
from coomon.models import Timestamped


# Create your models here.
class Author(Timestamped):
    name = models.CharField(max_length=200)
    birth_year = models.IntegerField()
    death_year = models.IntegerField(blank=True, null=True)
    bioream = models.TextField()

    def __str__(self):
        return f"{self.name}  ({self.birth_year} - )"


class Book(Timestamped):
    authors = models.ManyToManyField(Author, related_name="books")
    title=models.CharField(max_length=255)
    description=models.TextField()
    available=models.BooleanField(default=True)
    publication_year=models.DateField(auto_now_add=False) # IntegerField()
    author_name=models.CharField(max_length=255)
    author_surname=models.CharField(max_length=255)
    tags = models.ManyToManyField("tags.Tag", related_name="books")
    def __str__(self):
        return f"{self.id} {self.title} available: {self.available}"

