
from kafka import KafkaProducer
from config import KAFKA_BROKER, TOPIC_OUTPUT
from models.sentiment_event import SentimentEvent
import json


class SentimentProducer:

    def __init__(self):
        self.producer = KafkaProducer(
            bootstrap_servers=KAFKA_BROKER,
            value_serializer=lambda m: json.dumps(m).encode("utf-8")
        )

    def send(self, event: SentimentEvent):
        self.producer.send(
            TOPIC_OUTPUT,
            value=event.model_dump()
        )
        self.producer.flush()