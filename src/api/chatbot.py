from fastapi import APIRouter
from pydantic import BaseModel

from src.services.retriever import Retriever

router = APIRouter()


class ChatbotParams(BaseModel):
    message: str
    session_id: str | None = None


@router.post("/chatbot")
async def chatbot(request_body: ChatbotParams):
    retriever = Retriever(
        message=request_body.message, session_id=request_body.session_id
    )
    retriever.retrieve_and_respond()
    formatted_response = retriever.format_result()
    return formatted_response
