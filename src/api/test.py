from fastapi import APIRouter, Response
from pydantic import BaseModel

router = APIRouter()


class POSTTest(BaseModel):
    message: str


@router.post("/test")
async def post_test(request_body: POSTTest):
    return Response(status_code=200, content=request_body.model_dump_json())
