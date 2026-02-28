from twilio.rest import Client

from config import settings


def _twilio_client() -> Client:
    return Client(settings.twilio_account_sid, settings.twilio_auth_token)


def _send_otp_console(phone: str, code: str, channel: str = "sms") -> None:
    print(f"[OTP-CONSOLE] channel={channel} phone={phone} code={code}")


def _send_otp_twilio(phone: str, code: str, channel: str = "sms") -> None:
    if not settings.twilio_account_sid or not settings.twilio_auth_token or not settings.twilio_phone_number:
        raise RuntimeError("Twilio is not configured. Set TWILIO_* env vars.")

    body = f"Your OTP is {code}. Valid for {settings.otp_ttl_seconds // 60} min."
    from_addr = settings.twilio_phone_number

    if channel == "whatsapp":
        from_addr = f"whatsapp:{from_addr}"
        phone = f"whatsapp:{phone}"

    _twilio_client().messages.create(
        body=body,
        from_=from_addr,
        to=phone,
    )


def send_otp(phone: str, code: str, channel: str = "sms") -> None:
    provider = (settings.otp_provider or "console").lower().strip()
    if provider == "twilio":
        _send_otp_twilio(phone, code, channel)
        return
    _send_otp_console(phone, code, channel)
