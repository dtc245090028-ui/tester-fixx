import pytest
from datetime import datetime, timezone
from types import SimpleNamespace
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.main import app
from app.core import rbac
from app.core.database import Base, engine, SessionLocal
from app.models.user import User
from app.models.station import Station
from app.api.deps import get_current_user, get_current_active_user


def test_station_example():
    """Hàm test sử dụng các import để chỉ có Station là unused."""
    client = TestClient(app)
    now = datetime.now(timezone.utc)
    ns = SimpleNamespace(created=now)
    db: Session = SessionLocal()
    try:
        user = User(username="test_station_user")
        _ = (client, ns, db, user, Base, engine, rbac, get_current_user, get_current_active_user)
        assert pytest is not None
    finally:
        db.close()
