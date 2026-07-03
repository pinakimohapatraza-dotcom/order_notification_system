import boto3

from app.core.config import settings


def get_sqs_client():
    return boto3.client(
        "sqs",
        region_name=settings.aws_region,
    )