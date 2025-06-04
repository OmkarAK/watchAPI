from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, schemas
from database import SessionLocal

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def root():
    return {"message":"API health check successful"}

@app.get("/v0/built", response_model=list[schemas.built])
def read_builts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_builts(db, skip=skip, limit=limit)

# @app.get("/v0/built/{serial}",response_model=schemas.built)
# def read_built(serial:int,db:Session = Depends(get_db)):
#     built = crud.get_built(db, serial=serial)
#     if built is None:
#         raise HTTPException(status_code=404, detail="Built not found")
    
#     return built

@app.get("/v0/num", response_model=list[schemas.num])
def read_num(skip: int = 0, limit:int = 100, db: Session= Depends(get_db)):
    num = crud.get_num(db, skip=skip, limit=limit)
    return num