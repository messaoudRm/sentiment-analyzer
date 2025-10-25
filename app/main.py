from fastapi import FastAPI


app = FastAPI(
    title="Sentiment Analyzer Microservice",
    description="Microservice REST conteneurisé pour l’analyse de sentiment à l’aide de Hugging Face Transformers.",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"message": "Sentiment Analyzer Microservice is running"}
