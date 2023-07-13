from django.shortcuts import render, HttpResponse
# Create your views here.
layout = """
    <h1> Listado de carreras</h1>
 
    """

def index(request):
    
    return render(request,'index.html')

def saludo(request):
    return render(request,'saludo.html')


    
def rango(request):
    return render(request,'rango.html')

def rango2(request):
    return render(request,'rango2.html')   

def rango3(request):
    return render(request,'rango3.html')   