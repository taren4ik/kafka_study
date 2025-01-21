import pandas as pd
from fastapi import FastAPI
from typing import Optional, Union
import json
import pickle
from schema import MlRequest


from forest_model import model_leaner

import ssl

ssl._create_default_https_context = ssl._create_default_https_context

app = FastAPI()

with open('../model.pkl', 'rb') as f:
    model_forest = pickle.load(f)


def predict(age, sex, bml, bp, s1, s2, s3, s4, s5, s6):
    prediction = model_leaner.predict(pd.DataFrame([[age, sex, bml, bp, s1,
                                                     s2, s3, s4, s5, s6]]),
                                      columns=['age',
                                               'sex',
                                               'bml',
                                               'bp',
                                               's1',
                                               's2',
                                               's3',
                                               's4',
                                               's5',
                                               's6'])


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.post("/model-predict")
async def ml_predict(parametrs: MlRequest):
    return predict(parametrs.age, parametrs.sex, parametrs.bmi, parametrs.bp,
                   parametrs.age, parametrs.s1, parametrs.s2, parametrs.s3,
                   parametrs.s4, parametrs.s5, parametrs.s6)