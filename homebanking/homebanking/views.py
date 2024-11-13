from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def solicitar_prestamo(request):
    # Lógica para la vista de solicitud de préstamo
    return render(request, 'prestamo/solicitar_prestamo.html')
