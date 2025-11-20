from fastapi import FastAPI, Request
import httpx, os

app = FastAPI(title="psg-mock-router")

DOMAIN_URL = os.getenv("DOMAIN_MS_URL", "http://domain:8003")

@app.post("/route/account/load")
async def psg_route(request: Request):
    payload = await request.json()
    target = DOMAIN_URL + "/account/load"
    async with httpx.AsyncClient() as client:
        resp = await client.post(target, json=payload, timeout=10.0)
    return resp.json()

@app.get("/health")
async def health():
    return {"status": "psg-up"}
