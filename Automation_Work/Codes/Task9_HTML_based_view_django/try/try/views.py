from django.shortcuts import render
# import requests
import sys
from subprocess import run, PIPE


def button(request):
    return render(request, 'home.html')


def external(request):
    days = request.POST.get('days')
    tog = request.POST.get('tog')
    image = run([sys.executable, 'C://Users//Shreya Sinha//PycharmProject//Shreya//django_main.py', str(tog), str(days)],
                shell=False, stdout=PIPE)

    # return render(request, 'home.html', {'edit_url': image.stdout})
    return render(request, 'home.html')