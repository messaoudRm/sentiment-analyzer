
# NLP Model
MODEL_NAME = "distilbert-base-uncased-finetuned-sst-2-english"

# FastAPI
APP_NAME = "Sentiment Analyzer Microservice"
APP_DESCRIPTION = "Microservice REST conteneurisé pour l’analyse de sentiment à l’aide de Hugging Face Transformers."
APP_VERSION = "1.0.1"

# Kafka
KAFKA_BROKER = "kafka:9092"
TOPIC_INPUT = "review.created"
TOPIC_OUTPUT = "sentiment.analyzed"
GROUP_ID = "fastapi-sentiment-group"