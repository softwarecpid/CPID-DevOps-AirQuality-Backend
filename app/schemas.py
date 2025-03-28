from datetime import time

from pydantic import BaseModel


# pydantic schema for coordinate responses
class AirQualityCoordinates(BaseModel):
    latitude: float
    longitude: float


# the output schema sent in the response
class SensorDataOut(AirQualityCoordinates):
    pm2_5: float
    time: time
    temperature: float
    humidity: float
    typical_particle_size: float
    uid: int
    aqi: tuple[int, str]
