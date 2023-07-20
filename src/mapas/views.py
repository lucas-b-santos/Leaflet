from django.shortcuts import render
from django.http import HttpResponse

def tela(request):
    return render(request, 'pagina.html')