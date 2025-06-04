from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import date

class built(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    serial : int
    brand : str
    movement : str
    case_material : str 
    bracelet_material : str
    gender : str
    shape : str 
    crystal : str
    dial : str 
    bracelet_color : str
    clasp : str 
    year : date

class num(BaseModel):
    serial:int
    brand:str
    gender:str
    price:float
    total_sale:int
    seller_reviews:int
    year:date
    volume:str