from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from tuites.models import Tuite


# Create your views here.
def index(request):
    context = {
        "now": datetime.now(),
        "tuites": Tuite.objects.all(), 
    }
    return render(request, 'home.html', context)