from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline


app = FastAPI(
    title="Sentiment Analyzer Microservice",
    description="Microservice REST conteneurisé pour l’analyse de sentiment à l’aide de Hugging Face Transformers.",
    version="1.0.0"
)

modelName = "distilbert-base-uncased-finetuned-sst-2-english"
sentimentPipeline = pipeline("sentiment-analysis", model=modelName)

class TextInput(BaseModel):
    text: str

@app.get("/")
def root():
    return {"message": "Sentiment Analyzer Microservice is running"}


@app.post("/analyze")
def analyzeSentiment(input: TextInput):
    result = sentimentPipeline(input.text)[0]
    return {
        "label": result["label"],
        "score": round(result["score"], 4)}
