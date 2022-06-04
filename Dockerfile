FROM python:3.8.1-slim

WORKDIR /app

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y

COPY ./ /app
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r requirements.txt

CMD ["dvc","pull","-r","model-tracker-gcp"]

EXPOSE 8000

CMD ["./start.sh"]
