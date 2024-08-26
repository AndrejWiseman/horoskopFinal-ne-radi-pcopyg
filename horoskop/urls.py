from django.urls import path
from .views import home, horoskop, prikazi_znak


urlpatterns = [
    path('', home, name='home'),

    path('<str:znak>/', horoskop, name='horoskop'),
    path('znak/<str:znak>/', prikazi_znak, name='prikazi_znak'),

]