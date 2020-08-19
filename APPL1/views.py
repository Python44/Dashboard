from django.shortcuts import render, get_object_or_404
from .models import Device_String
from django.urls import path

from django.http import HttpResponse


def home(request):
    Device_Strings = Device_String.objects.all().order_by('Name')
    return render(request, 'APPL1/home.html', {'Device_Strings' : Device_Strings})

def Device_details(request, pk):
    Device_Strings = Device_String.objects.get(Name=pk)
    return render(request, 'APPL1/Device_details.html', {'Device_Strings' : Device_Strings})
#    return HttpResponse("You're looking at question %s." % pk)
