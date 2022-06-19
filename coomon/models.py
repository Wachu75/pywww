from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now, timedelta


# Create your models here.
class CheckAgeMixin:
    def is_older_then_n_days(self, n=1):
        delta = timedelta(days=n)
        return now() - self.created > delta

class Timestamped(models.Model, CheckAgeMixin):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateField(auto_now=True)

    class Meta:
        abstract = True
