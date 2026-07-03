from fastapi import APIRouter
from fastapi import Depends

from app.schemas.order import OrderRequest
from app.dependencies.services import get_order_service
from app.services.order_service import OrderService

router = APIRouter(prefix="/orders", tags=["Orders"])


@router.post("")
async def create_order(
    order: OrderRequest,
    service: OrderService = Depends(get_order_service),
):
    return service.create_order(order)