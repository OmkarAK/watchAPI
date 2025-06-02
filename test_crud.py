import pytest
from datetime import date

import crud
from database import SessionLocal

@pytest.fixture(scope='function')
def db_session():
    session = SessionLocal()
    yield session
    session.close()

def test_get_built(db_session):
    serials = crud.get_built(db_session,serial = 12)
    assert serials.serial == 12 

def test_get_num(db_session):
    serials = crud.get_num(db_session,serial = 12)
    assert serials.serial == 12 