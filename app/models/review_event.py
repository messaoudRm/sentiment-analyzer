
from pydantic import BaseModel

class ReviewEvent(BaseModel):
    reviewId: int
    movieId: int
    text: str
