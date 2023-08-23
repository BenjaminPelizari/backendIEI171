from django.http import HttpResponse

def saludo(request):
    docum = ("<h1>Hola profesor Bienvenido a mi Dasdas  JANGO</h1>")
    return HttpResponse(docum)

def nosvemos(request):
    return HttpResponse("Hola Rodolfo")