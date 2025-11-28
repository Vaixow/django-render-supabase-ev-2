from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"groups", views.GroupViewSet)
router.register(r"contacto", views.ContactoViewSet)

urlpatterns = [
    # URLs de AUTENTICACIÓN de Django (¡Solución al 404!)
    # Esto agrega /accounts/login/, /accounts/logout/, /accounts/password_change/, etc.
    path('accounts/', include('django.contrib.auth.urls')), 
    
    # Tus URLs existentes
    path('', views.lista_contactos, name='lista_contactos'),
    path('agregar/', views.agregar_contacto, name='agregar_contacto'),
    path('editar/<int:pk>/', views.editar_contacto, name='editar_contacto'),
    path('eliminar/<int:pk>/', views.eliminar_contacto, name='eliminar_contacto'),
    path("api/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]