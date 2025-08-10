from fastapi import FastAPI, Header, HTTPException
from fastapi.responses import JSONResponse
import os

app = FastAPI(title="Assistant Copro API", version="0.1.1")

# Accepte GET et HEAD (utile pour curl -I /health)
@app.api_route("/health", methods=["GET", "HEAD"])
def health():
    return JSONResponse({"status": "ok", "version": os.getenv("APP_ENV", "dev")})

@app.post("/auth/verify")
def auth_verify(authorization: str = Header(None)):
    # LOT 1: stub — valide seulement la présence du header
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing or invalid token")
    # LOT 2+: vérifier RS256 via JWKS, scopes, exp/iat, etc.
    return {"ok": True, "role": "stub", "group_id": None, "scopes": ["read"]}

