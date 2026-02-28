from pydantic import BaseModel, Field


class SendOtpRequest(BaseModel):
    phone: str = Field(..., description="E.164 number, e.g. +919999999999")
    channel: str = Field(default="sms", description="sms or whatsapp")


class SendOtpResponse(BaseModel):
    success: bool
    message: str


class VerifyOtpRequest(BaseModel):
    phone: str
    code: str = Field(..., min_length=4, max_length=10)


class VerifyOtpResponse(BaseModel):
    success: bool
    message: str
    firebase_custom_token: str | None = None
