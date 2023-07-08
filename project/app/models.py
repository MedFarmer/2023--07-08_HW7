from django.db import models
from django.core import validators

class Hotels(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(validators=[validators.MinLengthValidator(100)])
    date_openning = models.DateField()
            
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "complete/%s" % self.pk  
 