from fastapi.testclient import TestClient
from Main import app

client = TestClient(app)

def test_hired_by_quarter():
    response = client.get("/metrics/contrataciones_por_trimestre_2021")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    print("Test contrataciones_por_trimestre_2021 ejecutado con éxito")

def test_departments_above_average():
    response = client.get("/metrics/departamentos_sobre_promedio")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    print("Test departamentos_sobre_promedio ejecutado con éxito")