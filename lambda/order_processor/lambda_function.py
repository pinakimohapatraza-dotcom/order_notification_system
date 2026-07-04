import json
import logging

from app.constants.event_type import EventType
from app.core.context import reset_request_id
from app.core.context import set_request_id
from app.schemas.event import OrderCreatedEvent
from app.services.sns_service import SNSService

logger = logging.getLogger(__name__)

sns_service = SNSService()


def lambda_handler(event, context):

    for record in event["Records"]:

        body = json.loads(record["body"])

        message = OrderCreatedEvent.model_validate(body)

        token = set_request_id(message.request_id)
        subject = ""
        if message.event_type == EventType.ORDER_CREATED:
            subject = "Order Created"
            dgvdfg=0

        try:

            logger.info(
                "Processing event %s",
                message.event_id,
            )

            sns_service.publish(
                subject=subject,
                message=message.model_dump(mode="json"),
            )

        finally:

            reset_request_id(token)

    return {
        "statusCode": 200
    }