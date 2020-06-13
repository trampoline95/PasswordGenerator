from django.shortcuts import render
import random
from django.http import HttpResponse


# Create your views here.

def home(request):
    return render(request, 'generator/home.html', )


def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('number'):
        characters.extend(list('1234567890'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))

    length = int(request.GET.get('length'))

    thepassword = ''

    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, "generator/password.html", {'password': thepassword})
