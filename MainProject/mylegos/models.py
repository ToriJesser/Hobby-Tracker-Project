from django.db import models

class LegoSet(models.Model):

    set_name = models.CharField(max_length=30)
    theme = models.CharField(max_length=20)
    release_date = models.CharField(max_length=20)
    num_parts_need = models.CharField(max_length=10, blank=True)
    price = models.CharField(max_length=10, blank=True)

    LegoSets = models.Manager()

    def __str__(self):
        return self.set_name


