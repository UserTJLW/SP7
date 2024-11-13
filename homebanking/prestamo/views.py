from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PrestamoForm
from .models import Prestamo

@login_required
def solicitar_prestamo(request):
    cliente = request.user.cliente  # Suponiendo que Cliente tiene una relación 1:1 con User
    
    # Procesar el formulario al recibir una solicitud POST
    if request.method == 'POST':
        form = PrestamoForm(request.POST, cliente=cliente)
        if form.is_valid():
            prestamo = form.save(commit=False)
            prestamo.cliente = cliente
            
            # Lógica de aprobación del préstamo
            if cliente.tipo_cliente == 'BLACK' and form.cleaned_data['loan_total'] <= 500000:
                prestamo.aprobado = True
            elif cliente.tipo_cliente == 'GOLD' and form.cleaned_data['loan_total'] <= 300000:
                prestamo.aprobado = True
            elif cliente.tipo_cliente == 'CLASSIC' and form.cleaned_data['loan_total'] <= 100000:
                prestamo.aprobado = True
            else:
                prestamo.aprobado = False  # El préstamo se rechaza si el monto excede el límite

            prestamo.save()
            return redirect('prestamo:exito')  # Redirigir a una página de éxito
    else:
        form = PrestamoForm(cliente=cliente)

    return render(request, 'prestamo/solicitar_prestamo.html', {'form': form})


