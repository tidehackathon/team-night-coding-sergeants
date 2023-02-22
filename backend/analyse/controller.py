import operator
from fastapi import APIRouter, HTTPException, status
from .model import NewsModel, ReturnNewsModel, ReturnTwitterStatsModel

router = APIRouter(
    prefix='/analyse',
    tags=['analyse']
)


@router.get('/')
async def analyse_get():
    return {
        'message': 'its working'
    }


@router.post('/news')
async def analyse_post(news: NewsModel):
    # TODO: Analiza przez wszystkie modele

    result = ReturnNewsModel()

    return {
        'prediction': result
    }


@router.post('/twitter')
async def analyse_twitter(file):
    # TODO: Analiza pliku twitterowego

    result = ReturnTwitterStatsModel()

    return{
        'prediction': result
    }

