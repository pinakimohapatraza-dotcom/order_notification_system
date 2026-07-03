import json

import logging
from botocore.exceptions import BotoCoreError, ClientError

from app.clients.sqs_client import get_sqs_client
from app.core.config import settings




logger = logging.getLogger(__name__)
class SQSService:
    """Handles all interactions with Amazon SQS."""

    def __init__(self) -> None:
        self.client = get_sqs_client()
        self.queue_url = settings.sqs_queue_url

    def publish(self, message: dict) -> str:
        """
        Publish a message to SQS.

        Returns:
            MessageId returned by SQS.
        """
        try:
            response = self.client.send_message(
                QueueUrl=self.queue_url,
                MessageBody=json.dumps(message),
            )
            logger.info("SQS Response: %s", response)

            message_id = response["MessageId"]

            logger.info("Message published to SQS: %s", message_id)

            return message_id

        except (ClientError, BotoCoreError):
            logger.exception("Failed to publish message to SQS")
            raise