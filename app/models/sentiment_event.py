
from pydantic import BaseModel

class SentimentEvent(BaseModel):
    reviewId: int
    sentiment: str
    score: float
