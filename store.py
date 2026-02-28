from datetime import datetime, timedelta, UTC
import secrets

from config import settings


_otp_store: dict[str, tuple[str, datetime]] = {}


def generate_code() -> str:
    return f"{secrets.randbelow(900000) + 100000}"


def save_code(phone: str, code: str) -> None:
    expires = datetime.now(UTC) + timedelta(seconds=settings.otp_ttl_seconds)
    _otp_store[phone] = (code, expires)


def verify_code(phone: str, code: str) -> bool:
    rec = _otp_store.get(phone)
    if not rec:
        return False
    saved, exp = rec
    if datetime.now(UTC) > exp:
        _otp_store.pop(phone, None)
        return False
    if saved != code:
        return False
    _otp_store.pop(phone, None)
    return True
