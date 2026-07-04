import json
import logging

from botocore.exceptions import ClientError

from app.clients.sns_client import get_sns_client
from app.core.config import settings

logger = logging.getLogger(__name__)


class SNSService:

    def __init__(self):
        self.client = get_sns_client()
        self.topic_arn = settings.sns_topic_arn

    def publish(self, subject: str, message: dict):

        response = self.client.publish(
            TopicArn=self.topic_arn,
            Subject=subject,
            Message=json.dumps(message),
        )

        logger.info(
            "Published SNS message %s",
            response["MessageId"],
        )

        return response["MessageId"]