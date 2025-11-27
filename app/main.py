from fastapi import FastAPI
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
from starlette.responses import Response

app = FastAPI()

# Custom metric: how many times / was called
REQUESTS_TOTAL = Counter("app_requests_total", "Total number of requests to the root endpoint")


@app.get("/")
def root():
    REQUESTS_TOTAL.inc()
    return {"message": "Hello from CERN observability lab"}


@app.get("/metrics")
def metrics():
    data = generate_latest()
    return Response(content=data, media_type=CONTENT_TYPE_LATEST)

