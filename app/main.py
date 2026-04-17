from fastapi import FastAPI
from config import APP_NAME, APP_DESCRIPTION, APP_VERSION
from kafka_client.consumer import ReviewConsumer
import threading

app = FastAPI(
    title=APP_NAME,
    description=APP_DESCRIPTION,
    version=APP_VERSION
)

consumer = ReviewConsumer()

# Kafka consumer thread
def run_consumer():
    consumer.start()


@app.get("/")
def root():
    return {"message": "Sentiment Analyzer Microservice is running"}


@app.on_event("startup")
def startup():
    thread = threading.Thread(target=run_consumer)
    thread.daemon = True
    thread.start()
