from fastapi import FastAPI

app:FastAPI = FastAPI(
    title="Kami Room Chat Demo",
    description="A demo application for Kami Room Chat using NATS",
    version="0.1.0",
)