from pydantic import BaseModel
from typing import List



class ReturnNewsModel(BaseModel):
    predict_logistic: int
    predict_decision_tree:int


class ReturnTwitterStatsModel(BaseModel):
    verifiedUsers: int = 100
    verifiedTrue: int = 1000
    verifiedFalse: int = 3000
    unverifiedUsers: int = 400
    unverifiedTrue: int = 2000
    unverifiedFalse: int = 6000
