import sys
sys.path.insert(1, './src')

from fastapi import FastAPI, status, File, UploadFile
from fastapi.responses import HTMLResponse
#from .app.views import predict_land_cover

import logging
from logging.config import dictConfig
from .app.log_config import log_config 

dictConfig(log_config)
logger = logging.getLogger("model_predict") # should be this name unless you change it in log_config.py

logger.info('Starting Fast API')
app = FastAPI()


@app.get('/healthcheck', status_code=status.HTTP_200_OK)
def perform_healthcheck():
    logger.info('Healthcheck ok')
    return {'healthcheck': 'Ok'}

@app.get("/")
def main():
    logger.info('Accessing root')
    content = """
<body>
<p>Hello World !</p>
</body>
    """
    return HTMLResponse(content=content)

@app.post("/v1/predict_image_label")
def get_prediction(file: UploadFile = File(...)):
    logger.info('Predicting image')
    logger.info('Reading image')
    image_file = file.read()
    logger.info('Predicting image')
    prediction = predict_land_cover(image_file)
    return prediction
