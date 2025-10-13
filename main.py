from fastapi import FastAPI
from routers import messages

app = FastAPI(
    title="Chatting Service",
    description="Handles user-to-user messages",
    version="1.0.0"
)

app.include_router(messages.router)

@app.get("/")
def root():
    return {"status": "Chatting Service running"}
