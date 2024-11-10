from django.db import models


# Create your models here.
class Driver(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    truckNumber = models.IntegerField()
    hireDate = models.DateField(null=True)
    phoneNumber = models.PositiveIntegerField(null=True)

    def __str__(self):
        return f"{self.truckNumber}   {self.firstName} {self.lastName}"
    
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Driver'
        verbose_name_plural = 'Drivers'
        ordering = ("lastName", "firstName")
