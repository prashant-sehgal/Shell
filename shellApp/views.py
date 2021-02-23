from django.shortcuts import render
import subprocess

# Create your views here.

def home(request):
    return render(request, 'index.html', {'commandPannel': ''})

def issueCommand(request):
    command = request.POST['command']
    direct_output = subprocess.check_output(command, shell=True)
    return render(request, 'index.html', {'commandPannel': direct_output})