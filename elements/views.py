from django.shortcuts import render


def home(request):
    return render (request, 'resume/home.html')

def sertificat(request):
    return render(request, 'resume/sertificat.html')

def contacts(request):
    return render (request, 'resume/contacts.html')

def full(request):
    return render (request, 'resume/full.html')

def samples(request):
    return render(request, 'resume/samples.html')

def my_teaching(request):
    return render(request, 'resume/my_teaching.html')

