from django.db import models
from django.utils import timezone
import datetime

# now = datetime.datetime.now()
# Create your models here.
class TitanicDb(models.Model):
    pclass = models.CharField(max_length=3, default='0')
    sex = models.CharField(max_length=3, default='0')
    age = models.CharField(max_length=2, default='0')
    sibhp = models.CharField(max_length=3, default='0')
    parch = models.CharField(max_length=3, default='0')
    fare = models.CharField(max_length=3, default='0')
    mbarked = models.CharField(max_length=3, default='0')
    title = models.CharField(max_length=30, default='0')

    skl_result = models.CharField(max_length=30, default='0')
    nn_result = models.CharField(max_length=30, default='0')
    nn_rate = models.CharField(max_length=30, default='0')

    completed = models.BooleanField(default=True)
    # date_time = models.DateTimeField(default=timezone.now)
    date_time = models.DateTimeField(default=datetime.datetime.now())


    def __str__(self):
        return '%s' % (self.id)
