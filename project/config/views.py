from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Hola Django")

def saludo_con_input(request):
    nombre = input(" Ingrese su nombre: ")
    return HttpResponse(f"Hola {nombre}")
