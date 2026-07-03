from fastapi import status

from app.exceptions.base import AppException


class OrderPublishException(AppException):

    def __init__(self):

        super().__init__(
            message="Unable to publish order",
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )