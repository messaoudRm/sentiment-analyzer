
from kafka import KafkaConsumer
from config import KAFKA_BROKER, TOPIC_INPUT, GROUP_ID
from models.review_event import ReviewEvent
from models.sentiment_event import SentimentEvent
from services.sentiment_service import SentimentService
from kafka.producer import SentimentProducer
import json


class ReviewConsumer:

    def __init__(self):
        self.consumer = KafkaConsumer(
            TOPIC_INPUT,
            bootstrap_servers=KAFKA_BROKER,
            group_id=GROUP_ID,
            auto_offset_reset="earliest",
            enable_auto_commit=True,
            value_deserializer=lambda m: json.loads(m.decode("utf-8"))
        )

        self.service = SentimentService()
        self.producer = SentimentProducer()

    def start(self):
        print("Kafka Consumer started...")

        for message in self.consumer:
            try:
                # Parse event
                review = ReviewEvent(**message.value)

                # NLP sur le texte
                result = self.service.analyze(review.text)

                # Construire l'event de sortie
                sentiment_event = SentimentEvent(
                    reviewId=review.reviewId,
                    sentiment=result["label"],
                    score=float(result["score"])
                )

                # Publish sur Kafka
                self.producer.send(sentiment_event)

            except Exception as e:
                print(f"Error processing message: {e}")