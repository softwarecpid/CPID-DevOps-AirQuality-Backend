# from datetime import date

from fastapi import status
from fastapi.testclient import TestClient

# from app.schemas import SensorDataOut


def test_get_data(client: TestClient):
    res = client.get(
        "/sensorData",
        params={
            "date_reference": "2024-10-04",
            "start_time": "07:00:00",
            "end_time": "23:59:59",
        },
    )

    # data = SensorDataOut(**res.json())

    assert res.status_code == status.HTTP_200_OK
    # assert data.data.get("date") == date(2024, 10, 4)


def test_retreive_coordinates(client: TestClient):
    res = client.get(
        "/sensorData/coordinates",
        params={
            "date_reference": "2024-10-04",
            "start_time": "07:00:00",
            "end_time": "23:59:59",
        },
    )

    assert res.status_code == status.HTTP_200_OK
