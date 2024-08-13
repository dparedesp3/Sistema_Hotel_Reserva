import pytest
from App_Hotel.models import Personal
from App_Hotel.services import PersonalService
from App_Hotel.repositories import PersonalRepository
from rest_framework.test import APIClient
from django.urls import reverse

# Pruebas de Modelos
@pytest.mark.django_db
def test_personal_creation():
    personal = Personal.objects.create(nombre="Juan Pérez", puesto="Recepcionista")
    assert personal.nombre == "Juan Pérez"
    assert personal.puesto == "Recepcionista"

# Pruebas de Servicios
@pytest.mark.django_db
def test_create_personal_service():
    service = PersonalService()
    personal = service.create_personal("Ana López", "Cocinera")
    assert personal.nombre == "Ana López"
    assert personal.puesto == "Cocinera"

