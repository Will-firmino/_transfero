from django.urls import path
from sistema import views

# Informa qual será a rota que irá chamar determinada view(função).
urlpatterns = [
    path('sistema/', views.index),
]