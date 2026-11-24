import os
import socket
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/info")
def get_info():
    return {
        "module": "api-backend",
        "version": os.getenv("APP_VERSION", "v1.0"),
        "deployed_by": os.getenv("DEPLOYED_BY", "manual"),
        "pod": socket.gethostname(),
    }
