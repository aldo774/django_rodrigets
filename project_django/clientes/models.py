from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=6, decimal_places=2)
    bio = models.TextField()    
    photo = models.ImageField(upload_to='clientes_photo', blank=True, null=True)
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name
