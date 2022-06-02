FROM python:3.8.1-slim

WORKDIR /app

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y

COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./src ./src
COPY ./model ./model

COPY ./start.sh .

EXPOSE 8000

CMD ["./start.sh"]
