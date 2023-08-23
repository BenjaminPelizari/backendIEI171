from django.http import HttpResponse

def saludo(request):
    return HttpResponse("<h1>Hola profesor Bienvenido a mi DJANGO</h1>")

def nosvemos(request):
    return HttpResponse("Hola Rodolfo")