from django.urls import path
from . import views

app_name = 'prestamo'

urlpatterns = [
    path('solicitar/', views.solicitar_prestamo, name='solicitar_prestamo'),
]
