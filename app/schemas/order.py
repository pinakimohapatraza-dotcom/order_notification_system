from pydantic import BaseModel, EmailStr


class OrderRequest(BaseModel):
    order_id: str
    customer_name: str
    customer_email: EmailStr
    amount: float


class OrderResponse(BaseModel):
    message: str