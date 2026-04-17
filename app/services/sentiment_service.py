
from transformers import pipeline
from config import MODEL_NAME


class SentimentService:

    def __init__(self):
        self.pipeline = pipeline(
            "sentiment-analysis",
            model=MODEL_NAME
        )

    def analyze(self, text: str):
        return self.pipeline(text)[0]

