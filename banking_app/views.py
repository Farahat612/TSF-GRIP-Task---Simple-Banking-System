from django.shortcuts import render, redirect
from .models import Customer, Transfer
from decimal import Decimal
from django.contrib import messages  # Import messages
# Create your views here.




def home(request):
    return render(request, 'banking_app/home.html')

def view_customers(request):
    customers = Customer.objects.all()
    return render(request, 'banking_app/view_customers.html', {'customers': customers})

def view_customer(request, customer_id):
    customer = Customer.objects.get(pk=customer_id)
    return render(request, 'banking_app/view_customer.html', {'customer': customer})






from django.http import HttpResponseBadRequest

from django.http import HttpResponseBadRequest

def transfer_money(request):
    if request.method == 'POST':
        sender_id = request.POST['sender']
        receiver_id = request.POST['receiver']
        amount = Decimal(request.POST['amount'])

        sender = Customer.objects.get(pk=sender_id)
        receiver = Customer.objects.get(pk=receiver_id)

        # Check if the sender and receiver are the same customer
        if sender == receiver:
            error_message = "Cannot transfer money to yourself."
            return render(request, 'banking_app/error_message.html', {'error_message': error_message})

        if amount <= sender.balance:
            sender.balance -= amount
            receiver.balance += amount
            sender.save()
            receiver.save()

            transfer = Transfer(sender=sender, receiver=receiver, amount=amount)
            transfer.save()

            # Create a success message
            success_message = f"${amount} is successfully transferred from {sender.name} to {receiver.name}"
            messages.success(request, success_message)

            return redirect('view_customers')
        else:
            # Amount is greater than sender's balance
            error_message = "Not enough balance to make this transfer."
            return render(request, 'banking_app/error_message.html', {'error_message': error_message})

    customers = Customer.objects.all()
    return render(request, 'banking_app/transfer_money.html', {'customers': customers})
