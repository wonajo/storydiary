from django.shortcuts import render, get_object_or_404
from .models import storydiary
# Create your views here.
def home(request):
    storydiarys = storydiary.objects
    return render(request, 'home.html', {'storydiarys' :storydiarys})

def detail(request, storydiary_id):
    storydiary_detail = get_object_or_404(storydiary, pk = storydiary_id)
    return render(request, 'detail.html', {'storydiary' : storydiary_detail})