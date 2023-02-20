import operator
from fastapi import APIRouter, HTTPException, status
from .model import AnalyseModel

router = APIRouter(
    prefix='/analyse',
    tags=['analyse']
)

@router.get('/')
async def analyse_get():

    return {
        'message': 'its working'
    }

async def analyse_post(news:AnalyseModel):

    return {
        'message':'received analyse model'
    }