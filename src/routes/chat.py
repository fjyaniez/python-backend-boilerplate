from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse

from sqlmodel import Session

from typing import Annotated

from queue import Queue

from ..utils.config import Settings, get_settings
from ..utils.database import get_session

from ..services.langchain.chatbot_service import ChatbotService

router = APIRouter()

streamer_queue = Queue()


@router.get("/chatbot/{key}")
async def chat(*, key, message, session: Session = Depends(get_session),
               settings: Annotated[Settings, Depends(get_settings)]):
    service = ChatbotService(session=session, settings=settings, chatbot_key=key, streamer_queue=streamer_queue)
    return StreamingResponse(service.response_generator(message), media_type='text/event-stream')
