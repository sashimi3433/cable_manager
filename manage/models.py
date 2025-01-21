from django.db import models
from accounts.models import CustomUser

class Item(models.Model):

    name = models.CharField(max_length=50)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    date = models.DateField(null=True, blank=True)
    Manufacturer = models.CharField(max_length=25, null=True, blank=True)
    Store = models.CharField(max_length=25, null=True, blank=True)
    length = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
    watt = models.PositiveIntegerField(null=True, blank=True)
    PD = models.BooleanField(null=True, blank=True)
    thunderbolt = models.PositiveIntegerField(null=True, blank=True)
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name