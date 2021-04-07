from django.db import models
from django.conf import settings
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

class Post(models.Model):
  year = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(2021)])
  text = models.CharField("語呂合わせ", max_length=30)
  supplement = models.CharField("補足", max_length=100)
  author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  created = models.DateTimeField("作成日", default=timezone.now)

  def __str__(self):
    return str(self.year) + ' ' + self.text