from django.shortcuts import render
from django.http import HttpResponse

def cadastro(request):
    return HttpResponse ('Olá Mundo!!!')

# if request.method == 'GET':
# return render(request, 'cadastro.html')