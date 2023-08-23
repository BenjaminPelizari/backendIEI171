import datetime
from django.http import HttpResponse

def saludo(request):
    docum = ("<h1>Hola profesor Bienvenido a mi Dasdas  JANGO</h1>")
    return HttpResponse(docum)

def nosvemos(request):
    return HttpResponse("Hola Rodolfo")
def fechaactual(request):
    fecha_actual=datetime.datetime.now()
    docum= ("""<html> 
           <body>
           <h1> La fecha y hora es %s </h1>
           </body>
           </html>""" % fecha_actual)
    return HttpResponse(docum)
    
def calcularedad(request, edadactual, agno):
    #edadactual = 18
    periodo = agno - 2023
    edadfutura = edadactual + periodo
    docum= """<html> 
           <body>
           <h1> El año %s tendras %s </h1>
           </body>
           </html>""" % (agno, edadfutura)
    return HttpResponse(docum)