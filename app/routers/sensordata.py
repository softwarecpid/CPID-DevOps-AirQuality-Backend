from datetime import date, time
from typing import List

from app import models, schemas
from app.db.database import get_db
from app.utils import calc_aqi
from fastapi import APIRouter, Depends
from sqlalchemy import Row
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/sensorData",
    tags=["Sensor Data"],
)


# endpoint to get an payload of info about the air quality
# in determined period of time
@router.get("/", response_model=List[schemas.SensorDataOut])
def get_data(
    date_reference: date,
    start_time: time,
    end_time: time,
    db: Session = Depends(get_db),
):
    # get from the database all the fields we need
    resp: List[Row] = (
        db.query(
            models.AirQuality.latitude,
            models.AirQuality.longitude,
            models.AirQuality.pm2_5,
            models.AirQuality.time,
            models.AirQuality.temperature,
            models.AirQuality.humidity,
            models.AirQuality.typical_particle_size,
            models.AirQuality.uid,
        )
        # filter by the day and time reference
        .filter(
            models.AirQuality.date == date_reference,
            models.AirQuality.time.between(start_time, end_time),
        ).all()
    )

    return [
        {
            **obj._mapping,
            "aqi": calc_aqi(obj._mapping["pm2_5"]),
        }
        for obj in resp
    ]
