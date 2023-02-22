import operator
import pandas as pd
from fastapi import APIRouter, HTTPException, status, File, UploadFile
from .model import ReturnNewsModel, ReturnTwitterStatsModel
from ..functions.preprocessing_twitter_file import preproccessing_twitter_file
from ..functions.linear_regression_and_decision_tree import predict_file_linear_regression_and_decision_tree
from ..functions.linear_regression_and_decision_tree import learn_linear_regression_and_decisn_tree
from ..functions.linear_regression_and_decision_tree import predict_fact_linear_regression_and_decision_tree

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
async def analyse_post(news: str) -> ReturnNewsModel:
    # TODO: Analiza przez wszystkie modele
    predict_logistic, predict_decision_tree = predict_fact_linear_regression_and_decision_tree(news)

    return ReturnNewsModel(
        predict_logistic=predict_logistic,
        predict_decision_tree=predict_decision_tree
    )


@router.post('/twitter')
async def analyse_twitter(file: UploadFile = File(...)):
    df = pd.read_csv(filepath_or_buffer=file.file, encoding="utf-8",
                     engine='python', memory_map=True, on_bad_lines='skip', parse_dates=['date'])
    file.file.close()

    # TODO: Analiza pliku twitterowego
    verifiedUsers, verifiedTrue, verifiedFalse, unverifiedUsers, unverifiedTrue, unverifiedFalse=predict_file_linear_regression_and_decision_tree(df, file.filename)

    return ReturnTwitterStatsModel(
        verifiedUsers=verifiedUsers,
        verifiedTrue=verifiedTrue,
        verifiedFalse=verifiedFalse,
        unverifiedUsers=unverifiedUsers,
        unverifiedTrue=unverifiedTrue,
        unverifiedFalse=unverifiedFalse
    )

