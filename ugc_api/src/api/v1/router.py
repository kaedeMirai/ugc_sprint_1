from fastapi import APIRouter, Depends
from fastapi import HTTPException, status

from api.v1.schemas import NewMessage
from services.ugc_service import UgcService, get_ugc_service

router = APIRouter(prefix="/ugc", tags=["UGC"])


@router.post(
    "/send_event/{topic}",
    response_model=str,
    summary="Send new event to kafka topic",
    description="Send new event to kafka topic",
)
async def send_new_event(
        topic: str,
        message: NewMessage,
        ugc_service: UgcService = Depends(get_ugc_service)
):
    data = message.model_dump()
    data["topic"] = topic

    try:
        await ugc_service.send(topic=topic, message=message)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

    return 'Message sent successfully'
