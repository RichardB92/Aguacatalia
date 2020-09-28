from django.shortcuts import render

# Create your views here.


def home(request):
    context = {}
    return render(request, 'home.html')


def us(request):
    context = {}
    return render(request, 'us.html')


def coming(request):
    context = {}
    return render(request, 'coming.html')