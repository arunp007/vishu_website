from django.shortcuts import render
from django.http import HttpResponse

def vishu(request):
    return render(request,'vishu.html')

def astro(request):
    return render(request,'future.html')

