from pydantic import BaseModel
from typing import List


class NewsModel(BaseModel):
    text: str


class ReturnNewsModel(BaseModel):
    prediction: List[int] = []


class ReturnTwitterStatsModel(BaseModel):
    verifiedUsers: int = 100
    verifiedTrue: int = 1000
    verifiedFalse: int = 3000
    unverifiedUsers: int = 400
    unverifiedTrue: int = 2000
    unverifiedFalse: int = 6000
