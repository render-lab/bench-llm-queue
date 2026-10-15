import os

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from redis import Redis
from rq import Queue
from rq.job import Job

from jobs import summarize

redis = Redis.from_url(os.environ.get("REDIS_URL", "redis://localhost:6379"))
queue = Queue("summaries", connection=redis)

app = FastAPI(title="Seed LLM app")


class SummaryRequest(BaseModel):
    text: str


@app.post("/summaries")
def create_summary(body: SummaryRequest):
    job = queue.enqueue(summarize, body.text)
    return {"id": job.id}


@app.get("/summaries/{job_id}")
def get_summary(job_id: str):
    try:
        job = Job.fetch(job_id, connection=redis)
    except Exception:
        raise HTTPException(status_code=404)
    return {"status": job.get_status(), "summary": job.result}


@app.get("/health")
def health():
    redis.ping()
    return {"status": "ok"}
