import pytest
from App_Hotel.models import Huesped
from App_Hotel.services import HuespedService
from App_Hotel.repositories import HuespedRepository
from rest_framework.test import APIClient
from django.urls import reverse

# Pruebas de Modelos
@pytest.mark.django_db
def test_huesped_creation():
    huesped = Huesped.objects.create(nombre="Pedro", email="correo@prueba.com")
    assert huesped.nombre == "Pedro"
    assert huesped.email == "correo@prueba.com"

# Pruebas de Servicios
@pytest.mark.django_db
def test_create_huesped_service():
    service = HuespedService()
    huesped = service.create_huesped("Pablo", "prueba@correo.com")
    assert huesped.nombre == "Pablo"
    assert huesped.email == "prueba@correo.com"