# Seed: LLM app with a job queue

FastAPI web service that queues summarization jobs, and an RQ worker that runs
them against the OpenAI API. Needs Redis (`REDIS_URL`) and `OPENAI_API_KEY`.
No deploy config.

```bash
pip install -r requirements.txt
REDIS_URL=redis://localhost:6379 uvicorn app:app --reload
REDIS_URL=redis://localhost:6379 rq worker summaries
```
