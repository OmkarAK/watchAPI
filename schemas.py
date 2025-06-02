from pydantic import Basemodel, ConfigDict
from typing import List
from datetime import date

class built(Basemodel):
    model_config = ConfigDict(from_attributes=True)
    serial = int
    brand = str
    movement = str
    case = str 
    material = str
    bracelet_material = str
    gender = str
    shape = str 
    crystal = str
    dial = str 
    bracelet_color = str
    clasp = str 
    year = date

class num(Basemodel):
    serial:int
    brand:str
    gender:str
    price:int
    total_sale:int
    seller_reviews:int
    year:date
    volume:int