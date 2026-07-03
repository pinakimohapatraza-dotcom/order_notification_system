import uuid

from starlette.middleware.base import BaseHTTPMiddleware

from app.core.context import (
    set_request_id,
    reset_request_id,
)


class RequestIDMiddleware(BaseHTTPMiddleware):

    async def dispatch(
        self,
        request,
        call_next,
    ):

        request_id = request.headers.get(
            "X-Request-ID",
            str(uuid.uuid4()),
        )

        token = set_request_id(request_id)

        try:
            response = await call_next(request)

        finally:
            reset_request_id(token)

        response.headers["X-Request-ID"] = request_id

        return response