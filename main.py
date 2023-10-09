from fastapi import FastAPI
from dotenv import load_dotenv
load_dotenv()

from app.routes import webhook, test

app = FastAPI()

app.include_router(webhook.router)
app.include_router(test.router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)