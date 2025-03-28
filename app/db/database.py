from app.db.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Connection to the database
# In this case we are using MYSQL with MYSQLConnector
SQLACHEMY_DATABASE_URL = (
    f"mysql+mysqldb://"
    f"{settings.db_username}:{settings.db_password}"
    f"@{settings.db_hostname}:{settings.db_port}/{settings.db_name}"
)

engine = create_engine(SQLACHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base()


def get_db():
    """
    Function to connect with the database
    and close this connection when finished
    """

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
