from django.shortcuts import render
from .models import Articles


# Create your views here.
def index(request):
    art = Articles.objects.all()
    return render(request, 'home/index.html', {'art': art})
