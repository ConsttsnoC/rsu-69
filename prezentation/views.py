from django.shortcuts import render
from .models import Project

def home(requesr):
    projects = Project.objects.all()
    return render(requesr, 'prezentation/home.html',{'projects': projects})


def contact(requesr):
    return render(requesr, 'prezentation/contact.html')

def informaciya(requesr):
    return render(requesr, 'prezentation/informaciya.html')





