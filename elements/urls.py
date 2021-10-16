from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contacts', views.contacts, name='contacts'),
    path('full', views.full, name='full'),
    path('samples', views.samples, name='samples'),
    path('my_teaching', views.my_teaching, name='my_teaching'),
    path('sertificat', views.sertificat, name='sertificat'),
]