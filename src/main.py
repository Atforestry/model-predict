import sys
sys.path.insert(1, './src')

from fastapi import FastAPI, status, File, UploadFile
from fastapi.responses import HTMLResponse
from .app.views import predict_land_cover

import logging
from logging.config import dictConfig
from .app.log_config import log_config 

dictConfig(log_config)
logger = logging.getLogger("model_predict") # should be this name unless you change it in log_config.py

app = FastAPI(
    title='Atforesty Inference API',
    description='This web interface allows the user to load an image predict cover land type',
    version="1.0.0"
)


@app.get('/healthcheck', status_code=status.HTTP_200_OK)
def perform_healthcheck():
    logger.info('Healthcheck ok')
    return {'healthcheck': 'Ok'}

@app.get("/")
def main():
    content = """
<body>
<p>Hello World !</p>
</body>
    """
    return HTMLResponse(content=content)

@app.post("/v1/predict_image_label")
def get_prediction(file: UploadFile = File(...)):
    image_file = file.read()
    prediction = predict_land_cover(image_file)
    return prediction
