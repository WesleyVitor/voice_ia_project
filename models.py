from pydantic import BaseModel, Field

class GetBalanceRequest(BaseModel):
    ...

class PayInvoiceRequest(BaseModel):
    bolt11_str: str = Field(..., description="The BOLT11 invoice string to pay.")

class MakeInvoiceRequest(BaseModel):
    amount: int = Field(..., description="The amount in mSAT to create the invoice for.")

    description: str | None = Field(None, description="Optional description for the invoice.")
    description_hash: str | None = Field(None, description="Optional description hash for the invoice.")
    expiry: int | None = Field(None, description="Optional expiry time in seconds for the invoice.")