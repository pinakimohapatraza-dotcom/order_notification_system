import boto3

from app.core.config import settings


def get_sns_client():
    return boto3.client(
        "sns",
        region_name=settings.aws_region,
    )