import pytest
from fastapi.testclient import TestClient
from sqlalchemy import StaticPool, create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.db.database import Base, get_db
from app.main import app

SQLACHEMY_DATABASE_URL = "sqlite:///test/test.db"

engine = create_engine(
    SQLACHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)

TestingSessionLocal = sessionmaker(
    autoflush=False,
    autocommit=False,
    bind=engine,
)


Base.metadata.create_all(bind=engine)


@pytest.fixture(scope="function")
def session():
    """
    Create a new database session for a test.
    """
    connection = engine.connect()
    transaction = connection.begin()

    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        transaction.rollback()
        connection.close()


@pytest.fixture(scope="module")
def client(session: Session):
    def override_get_db():
        try:
            yield session
        finally:
            session.close()

    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)
