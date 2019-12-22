from django.db import models
import ggachi_backend.settings.base as settings
# Create your models here.
class Letter(models.Model):
    bride = models.CharField(max_length=50)
    groom = models.CharField(max_length=50)
    place_name = models.CharField(max_length=50)
    place_address = models.TextField()
    date = models.DateField()
    start_time = models.CharField(max_length=50)
    howtobus = models.TextField()
    howtosubway = models.TextField()
    message = models.TextField()
    template = models.IntegerField(default=1)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='letters', on_delete=models.CASCADE)
    