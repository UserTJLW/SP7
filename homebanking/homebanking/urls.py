from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views  # Importamos las vistas de autenticación

from . import views  # Asegúrate de tener un archivo views.py en el directorio correcto

urlpatterns = [
    # Página de inicio de la aplicación
    path('', views.home, name='home'),
    
    # URL para la administración de Django
    path('admin/', admin.site.urls),
    
    # URL para la autenticación de usuarios
    path('login/', auth_views.LoginView.as_view(), name='login'),  
    path('logout/', auth_views.LogoutView.as_view(), name='logout'), 
    path('prestamo/', include('prestamo.urls')),
    path('solicitar/', views.solicitar_prestamo, name='solicitar_prestamo'),
    
]



