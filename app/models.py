from sqlalchemy import (
    DECIMAL,
    BigInteger,
    Boolean,
    Column,
    Date,
    Integer,
    String,
    Time,
)

from app.db.database import Base

# Relational database models for each router


class AirQuality(Base):
    """
    Air Quality Model:

    Deals with every request made to the 'air_quality' table in the database.
    """

    __tablename__ = "air_quality"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)

    # sensor internal counter
    counter = Column(Integer)

    # coordinates of the sensor
    latitude = Column(DECIMAL(10, 6))
    longitude = Column(DECIMAL(10, 6))

    # tag to mark if the internal GPS of the sensor updated
    gpsUpdated = Column(Boolean)

    # the relative speed of the sensor
    speed = Column(DECIMAL(5, 2))

    # distance between the sea level and the sensor
    altitude = Column(DECIMAL(6, 2))

    satellites = Column(Integer)

    # date and time of the payload sent by the sensor
    date = Column(Date)
    time = Column(Time)

    millis = Column(BigInteger)

    # Particulate Matter followed by the max diamater of the particle
    pm1_0 = Column(DECIMAL(5, 2))
    pm2_5 = Column(DECIMAL(5, 2))
    pm4_0 = Column(DECIMAL(5, 2))
    pm10 = Column(DECIMAL(5, 2))

    # temperature and relative humidity in the air
    # in the moment the sensor sent the data
    temperature = Column(DECIMAL(5, 2))
    humidity = Column(DECIMAL(5, 2))

    nc0_5 = Column(DECIMAL(5, 2))
    nc1_0 = Column(DECIMAL(5, 2))
    nc2_5 = Column(DECIMAL(5, 2))
    nc4_0 = Column(DECIMAL(5, 2))
    nc10 = Column(DECIMAL(5, 2))

    # avarage particle size measured by the sensor
    typical_particle_size = Column(DECIMAL(5, 2))

    # Total Volatile Organic Compounds
    tvoc = Column(DECIMAL(5, 2))

    # Battery Voltage In
    battery_vin = Column(DECIMAL(5, 2))

    # compensated temperature and relative humidity
    compensated_t = Column(DECIMAL(5, 2))
    compensated_rh = Column(DECIMAL(5, 2))

    uid = Column(Integer)

    # city and state the sensor is located
    city = Column(String(250))
    state = Column(String(250))
