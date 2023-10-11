from django.db import models

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Transfer(models.Model):
    sender = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='sender_transfers')
    receiver = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='receiver_transfers')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender.name} to {self.receiver.name} - {self.amount}"
