import os

from dotenv import load_dotenv
from fastapi import Depends, FastAPI, Response
from sqlalchemy import text
from sqlalchemy.orm import Session

from src.db.config import get_db_session
from src.routes import app_router

load_dotenv()


app = FastAPI(
    title="BedRock RAG POC",
    debug=os.getenv("CURRENT_ENVIRONMENT", "") == "local",
)


@app.get("/health_check")
async def root(db: Session = Depends(get_db_session)):
    try:
        db.execute(text("SELECT 1"))
        return Response(status_code=200)
    except Exception:
        return Response(status_code=500, content="Database connection failed")


app.include_router(app_router)
