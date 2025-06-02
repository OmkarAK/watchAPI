from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload
from datetime import date

import models

def get_built(db:Session, serial: int):
    return db.query(models.Built).filter(models.Built.serial == serial).first()

def get_num(db:Session, serial: int):
    return db.query(models.Num).filter(models.Num.serial == serial).first()
