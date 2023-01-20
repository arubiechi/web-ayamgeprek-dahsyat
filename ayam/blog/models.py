from django.db import models
from datetime import datetime

# Create your models here.


class DaftarMenu(models.Model):
    makanan = models.CharField(max_length=255)
    harga = models.DecimalField(max_digits=6,decimal_places=0)
    gambar=models.ImageField()

    def __str__(self):
        return self.makanan

class Karyawan(models.Model):
    nama=models.CharField(max_length=100)
    jabatan=models.CharField(max_length=50)
    gambar=models.ImageField()

    def __str__(self):
        return self.nama

class Pesanan(models.Model):
    pass


class SavedCarts(models.Model):
    username = models.CharField(max_length=200, primary_key=True)
    cart = models.TextField() #this will be a string representation of the cart from localStorage

class UserOrder(models.Model):
    username = models.CharField(max_length=200) #who placed the order
    order = models.TextField() #this will be a string representation of the cart from localStorage
    price = models.DecimalField(max_digits=6, decimal_places=2) #how much was the order
    time_of_order  = models.DateTimeField(default=datetime.now, blank=True)
    delivered = models.BooleanField()

    class Meta:
        verbose_name = "User Order List"
        verbose_name_plural = "User Order List"

    def __str__(self):
        #overriding the string method to get a good representation of it in string format
        return f"Pesanan selesai  : {self.username} pada {self.time_of_order.date()} pukul {self.time_of_order.time().strftime('%H:%M:%S')}"
