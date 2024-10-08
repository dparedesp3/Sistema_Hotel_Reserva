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

# Pruebas de Repositorios
@pytest.mark.django_db
def test_get_all_personal_repository():
    repository = PersonalRepository()
    personal = repository.get_all()
    assert len(personal) == 0  # Asumiendo que la base de datos esté vacía al inicio de la prueba

# Pruebas de Controladores (ViewSets)
@pytest.mark.django_db
def test_get_personal_viewset():
    client = APIClient()
    response = client.get(reverse('personal-list'))
    assert response.status_code == 200
    assert response.json() == []

@pytest.mark.django_db
def test_create_personal_viewset():
    client = APIClient()
    data = {'nombre': 'María Rodríguez', 'puesto': 'Limpiadora'}
    response = client.post(reverse('personal-list'), data)
    assert response.status_code == 201
    assert response.json()['nombre'] == 'María Rodríguez'
    assert response.json()['puesto'] == 'Limpiadora'