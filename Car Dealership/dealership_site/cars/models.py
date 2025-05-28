from django.db import models
class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    image = models.ImageField(upload_to='cars/', null=True, blank=True)
    
    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"

class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    test_drive_date = models.DateField()
    def __str__(self):
        return f"{self.name} - {self.car}"
