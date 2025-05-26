from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
from typing import List

Base = declarative_base()

# SQLAlchemy Models
class CountryDB(Base):
    __tablename__ = "country"
    
    code = Column(String(2), primary_key=True, index=True)
    name = Column(String(100))

# Pydantic Models
class EnvironmentVar(BaseModel):
    key: str
    value: str

class Country(BaseModel):
    code: str
    name: str

class ApiResponse(BaseModel):
    environment: List[EnvironmentVar]
    secrets: List[EnvironmentVar]
    contries: List[Country]