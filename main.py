from fastapi import FastAPI, HTTPException

from firebase_auth import create_custom_token
from models import SendOtpRequest, SendOtpResponse, VerifyOtpRequest, VerifyOtpResponse
from providers import send_otp as send_otp_via_provider
from store import generate_code, save_code, verify_code

app = FastAPI(title="OTP Hub", version="0.1.0")


@app.get("/health")
def health():
    return {"ok": True, "service": "otp-hub"}


@app.post("/otp/send", response_model=SendOtpResponse)
def send_otp_handler(payload: SendOtpRequest):
    code = generate_code()
    save_code(payload.phone, code)
    try:
        send_otp_via_provider(payload.phone, code, payload.channel)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"OTP send failed: {e}")

    return SendOtpResponse(success=True, message="OTP sent")


@app.post("/otp/verify", response_model=VerifyOtpResponse)
def verify_otp(payload: VerifyOtpRequest):
    ok = verify_code(payload.phone, payload.code)
    if not ok:
        raise HTTPException(status_code=400, detail="Invalid or expired OTP")

    token = create_custom_token(payload.phone)
    return VerifyOtpResponse(success=True, message="OTP verified", firebase_custom_token=token)
