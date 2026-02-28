# OTP Hub (Railway-ready)

Production-style OTP service skeleton with:
- FastAPI API
- Provider abstraction (`console` free mode + Twilio)
- Firebase verification hook (optional)
- Env-based secrets

## Local run
```bash
python -m venv .venv
. .venv/Scripts/activate   # Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload --port 8000
```

## API
- `GET /health`
- `POST /otp/send`
- `POST /otp/verify`

## Zero-cost start (recommended)
1. Keep `OTP_PROVIDER=console` (default)
2. Deploy on Render free plan using `render.yaml`
3. Use `/otp/send` and read OTP from app logs (`[OTP-CONSOLE] ... code=123456`)

## Railway deploy (optional)
1. Push folder to repo
2. Create Railway project
3. Set env vars from `.env.example`
4. Deploy (uses `railway.json` start command)

## Upgrade path (when paid provider needed)
- Set `OTP_PROVIDER=twilio`
- Fill `TWILIO_*` env vars
- Redeploy

## Security notes
- Never put raw secrets in chat
- Rotate Twilio and Firebase credentials if leaked
- Add rate-limits + abuse controls before production
