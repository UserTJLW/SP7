from django import forms
from .models import Prestamo
from cliente.models import Cliente

class PrestamoForm(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = ['loan_total', 'loan_date', 'loan_type'] 

    def __init__(self, *args, **kwargs):
       
        self.cliente = kwargs.pop('cliente', None)
        super().__init__(*args, **kwargs)

    def clean_loan_total(self):
        monto = self.cleaned_data.get('loan_total') 
        tipo_cliente = self.cliente.tipo_cliente if self.cliente else None

       
        limites = {'BLACK': 500000, 'GOLD': 300000, 'CLASSIC': 100000}
        if tipo_cliente and monto > limites.get(tipo_cliente, 0):
            raise forms.ValidationError(f"El monto excede el límite permitido para su tipo de cliente ({tipo_cliente})")
        return monto
