from app.services.order_service import OrderService
from app.services.sqs_service import SQSService


def get_sqs_service() -> SQSService:
    return SQSService()


def get_order_service() -> OrderService:
    return OrderService(
        sqs_service=get_sqs_service()
    )