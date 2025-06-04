from sqlalchemy.orm import Session
import models

# def get_built(db:Session, serial: int):
#     return db.query(models.Built).filter(models.Built.serial == serial).first()

def get_builts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Built).offset(skip).limit(limit).all()

def get_num(db:Session, skip:int = 0, limit : int = 100):
    return db.query(models.Num).offset(skip).limit(limit).all()