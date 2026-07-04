from uuid import uuid4
import logging


from app.schemas.order import OrderRequest
from app.services.sqs_service import SQSService
from app.core.context import get_request_id
from app.constants.event_type import EventType



logger = logging.getLogger(__name__)


class OrderService:
    """Business logic related to orders."""

    def __init__(self, sqs_service: SQSService) -> None:
        self.sqs_service = sqs_service

    def create_order(self, order: OrderRequest) -> dict:
        logger.info("Processing order %s", order.order_id)
        request_id = get_request_id()

        message = {
            "event_id": str(uuid4()),
            "event_type": EventType.ORDER_CREATED,
            "payload": order.model_dump(mode="json"),
            "request_id": request_id,
        }

        message_id = self.sqs_service.publish(message)

        logger.info("Order queued successfully")

        return {
            "status": "queued",
            "message_id": message_id,
        }