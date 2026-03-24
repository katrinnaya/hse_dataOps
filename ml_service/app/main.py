from fastapi import FastAPI
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
from starlette.responses import Response
import logging
import json
import time
from datetime import datetime

app = FastAPI()
REQUEST_COUNT = Counter('api_requests_total', 'Total API requests')

logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(message)s')

@app.post("/api/v1/predict")
async def predict(data: dict):
    start = time.time()
    REQUEST_COUNT.inc()
    result = {"prediction": sum(data.values()) if all(isinstance(v, (int, float)) for v in data.values()) else 0}
    log_entry = {
        "input": data, 
        "output": result, 
        "time": datetime.now().isoformat(), 
        "version": "1.0",
        "latency_ms": (time.time() - start) * 1000
    }
    logging.info(json.dumps(log_entry))
    return result

@app.get("/metrics")
async def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)

@app.get("/health")
async def health():
    return {"status": "healthy"}
