''' Pydantic models that define the validation rules for the API.'''

from datetime import date
from typing import List, Optional
from pydantic import BaseModel

class CompanyBase(BaseModel):
    name: str
    reg_code: int
    start_date: date
    start_capital: int

class ShareHolder(BaseModel):
    id: int
    name: str
    person_code: int
    company_id: int
    founder: bool
    shares: int