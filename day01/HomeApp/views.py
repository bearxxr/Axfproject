from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from HomeApp.models import AxfWheel, AxfNav, AxfMustBuy, AxfMainShow


def test(request):
    return render(request,'axf/main/home/home.html')


def home(request):
    wheels = AxfWheel.objects.all()

    navs = AxfNav.objects.all()

    pigs = AxfMustBuy.objects.all()

    mainshows = AxfMainShow.objects.all()


    return render(request,'axf/main/home/home.html',context=locals())