from django.shortcuts import render
from django.http import HttpResponse
from ussd.responsegen import generate_response
# Create your views here.

# Welcome to GCWU Credit Union. What is your username?
# What is your password?
# Please select option? 1. Borrow Money 2. See Account Status
# Please select an amount
# Select payback period and interest rate
# %5 in 3 month, 10% 6, 15% 12
# Select destination bank account 1. TD 2. RBC
# Confirm 2 cancel
# Transaction complete

def index(request):
    response = ''
    if request.method == 'GET':
        d= request.GET
    elif request.method == 'POST':
        d = request.POST
        response = "Welcome to GCWU Credit Union.\n What is your username?"
        print(d['text'])
    return HttpResponse(generate_response(d['text']))