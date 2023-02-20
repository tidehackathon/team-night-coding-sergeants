from typing import Optional
from pydantic import BaseModel


class AnalyseModel(BaseModel):
    date: str
    header: str
    password: str