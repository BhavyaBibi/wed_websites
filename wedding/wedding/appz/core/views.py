from django.shortcuts import render
from django.conf import settings
from .models import Destination
# Create your views here.




def home(request):

    dests= Destination.objects.all()


    return render(request,'core/home.html',{'dests': dests})
