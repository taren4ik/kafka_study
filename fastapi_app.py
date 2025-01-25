from typing import Union

import pandas as pd
from fastapi import FastAPI
import pickle
from schema import MlRequest
from regression_model import model_linear
import ssl

ssl._create_default_https_context = ssl._create_default_https_context

app = FastAPI()

with open('model.pkl', 'rb') as f:
    model_leaner = pickle.load(f)


def predict(age, sex, bmi, bp, s1, s2, s3, s4, s5, s6):
    prediction = model_linear.predict(pd.DataFrame([[age, sex, bmi, bp, s1, s2, s3, s4, s5, s6]], columns=['age', 'sex', 'bmi', 'bp', 's1', 's2', 's3', 's4', 's5', 's6']))
    return prediction


# @app.get("/")
# def read_root():
#     return {"Hello": "World"}
#
#
# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}


@app.post("/model-predict", summary="Данные модели", tags=["Загрузка данных для расчета линейной регрессии"])
async def ml_predict(parameters: MlRequest):
      return  predict(parameters.age, parameters.sex, parameters.bmi, parameters.bp, parameters.s1, parameters.s2, parameters.s3, parameters.s4, parameters.s5, parameters.s6)[0]
