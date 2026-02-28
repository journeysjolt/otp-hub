import json

import firebase_admin
from firebase_admin import auth, credentials

from config import settings


def _ensure_firebase_init() -> bool:
    if firebase_admin._apps:
        return True
    if not settings.firebase_service_account_json:
        return False

    info = json.loads(settings.firebase_service_account_json)
    cred = credentials.Certificate(info)
    firebase_admin.initialize_app(cred, {"projectId": settings.firebase_project_id or info.get("project_id")})
    return True


def create_custom_token(phone: str) -> str | None:
    if not _ensure_firebase_init():
        return None
    uid = f"phone:{phone}"
    return auth.create_custom_token(uid).decode("utf-8")
