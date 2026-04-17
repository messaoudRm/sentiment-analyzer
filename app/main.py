from fastapi import FastAPI
from config import APP_NAME, APP_DESCRIPTION, APP_VERSION
from kafka.consumer import ReviewConsumer
import multiprocessing

app = FastAPI(
    title=APP_NAME,
    description=APP_DESCRIPTION,
    version=APP_VERSION
)

def run_consumer():
    consumer = ReviewConsumer()
    consumer.start()


@app.get("/")
def root():
    return {"message": "Sentiment Analyzer Microservice is running"}


@app.on_event("startup")
def startup():
    process = multiprocessing.Process(target=run_consumer)
    process.daemon = True
    process.start()
