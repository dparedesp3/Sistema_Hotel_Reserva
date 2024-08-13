import pytest
from App_Hotel.models import Reserva
from App_Hotel.services import ReservaService
from App_Hotel.repositories import ReservaRepository
from rest_framework.test import APIClient
from django.urls import reverse

# Pruebas de Modelos
@pytest.mark.django_db
def test_reserva_creation():
    reserva = Reserva.objects.create(fecha_entrada="2024-08-01", fecha_salida="2024-08-05")
    assert reserva.fecha_entrada == "2024-08-01"
    assert reserva.fecha_salida == "2024-08-05"

# Pruebas de Servicios
@pytest.mark.django_db
def test_create_reserva_service():
    service = ReservaService()
    reserva = service.create_reserva("2024-08-10", "2024-08-15")
    assert reserva.fecha_entrada == "2024-08-10"
    assert reserva.fecha_salida == "2024-08-15"

