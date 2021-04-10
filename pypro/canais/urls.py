from django.urls import path

from pypro.canais import views

app_name = 'canais'
urlpatterns = [
    path('', views.indice, name='indice'),
]
