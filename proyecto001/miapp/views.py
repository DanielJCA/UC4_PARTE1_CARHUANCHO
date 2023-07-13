from django.shortcuts import render, HttpResponse
# Create your views here.
layout = """
    <h1> Proyecto Web (LP3) | Flor Cerdán </h1>
    <hr/>
    <ul>
    <li>
    <a href="/inicio"> Inicio</a>
    </li>
    <li>
    <a href="/saludo"> Mensaje de Saludo</a>
    </li>
    <li>
    <a href="/rango"> Mostrar Números [a,b]</a>
    </li>
    </ul>
    <hr/>
    """

def index(request):
    
    return render(request,'index.html')

def saludo(request):
    return render(request,'saludo.html')

def rango(request):
    a = 10
    b = 20
    resultado = f"""
<h2> Numeros de [{a},{b}] </h2>
Resultado: <br>
<ul>
"""
    while a<=b:
        resultado += f"<li> {a} </li>"
        a+=1
    resultado += "</ul"
    return HttpResponse(layout + resultado)