from django.db import models

# Create your models here.
class first(models.Model):
    name1 = models.CharField(max_length=100)
    def __unicode__(self):
        return self.name1


