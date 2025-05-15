import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
import mlflow
import mlflow.pyfunc
from mlflow.models import Model
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

# uvicorn app:app --reload

app = FastAPI()

class Features(BaseModel):
    energy: float
    loudness: float
    speechiness: float
    acousticness: float
    instrumentalness: float
    liveness: float
    valence: float
    tempo: float
    duration: float
    year: float
    genre: str
    key: int
    time_signature: float
    mode: int

mlflow.set_tracking_uri("http://localhost:5000")
model_uri = 'mlflow-artifacts:/788248633673813493/ea0748f020b6464e9f4bedd6b4b273ab/artifacts/best_model'
pyfunc_model = mlflow.pyfunc.load_model(model_uri)

@app.post("/predict")
async def predict(features: Features):
    input_data = [[
        features.tempo,
        features.duration,
        features.energy,
        features.loudness,
        features.speechiness,
        features.acousticness,
        features.instrumentalness,
        features.liveness,
        features.valence,
        features.year,
        features.genre,
        features.key,
        features.time_signature,
        features.mode
    ]]
    columns = ['tempo', 'duration', 'energy', 'loudness',
        'speechiness', 'acousticness', 'instrumentalness', 'liveness',
        'valence', 'year', 'genre', 'key', 'time_signature', 'mode']
    df = pd.DataFrame(input_data, columns=columns)

    prediction = pyfunc_model.predict(df)

    return {'popular:': int(prediction[0])}









# df = df.astype({col: 'float64' for col in df.select_dtypes(include='int').columns})

# categorical = ['year', 'genre', 'key', 'time_signature', 'mode']
# numerical = ['tempo', 'duration', 'danceability', 'energy','loudness', 'speechiness', 'acousticness', 'instrumentalness',
#              'liveness', 'valence']
#
# numerical_pipeline = Pipeline([
#     ('imputer', SimpleImputer(strategy='median')),
#     ('scaler', StandardScaler())
# ])
#
# categorical_pipeline = Pipeline([
#     ('imputer', SimpleImputer(strategy='most_frequent')),
#     ('encoder', OneHotEncoder(handle_unknown='ignore', drop='first'))
# ])
#
# ct = ColumnTransformer(
#     force_int_remainder_cols=False,
#     transformers=[
#         ('num', numerical_pipeline, numerical),
#         ('cat', categorical_pipeline, categorical),
#     ],
#     remainder='passthrough'
# )
