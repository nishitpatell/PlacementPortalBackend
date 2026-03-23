import os
import tomllib
from fastapi import FastAPI
from app.routers import company_router

with open("pyproject.toml", "rb") as f:
    project_metadata = tomllib.load(f)["project"]

INSTANCE_NAME = os.getenv("INSTANCE_NAME", "Unknown Instance")

app = FastAPI(
    title = project_metadata.get("name", "Placement Portal API"),
    version = project_metadata.get("version", "0.1.0"),
    description = "Backend for the campus placement portal"
)

app.include_router(company_router.router)

@app.get("/")
def health_check():
    return {
        "status": "ok", 
        "message": "Placement Portal API is running",
        "instance_handled_by": INSTANCE_NAME 
    }