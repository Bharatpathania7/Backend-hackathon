from typing import List, Optional
from pydantic import BaseModel


class DetectRequest(BaseModel):
    user_id: str
    text: str
    volume: float
    repeat_count: int
    latitude: float
    longitude: float
    contacts: Optional[List[str]] = None


class DetectResponse(BaseModel):
    emergency: bool
    category: str
    confidence: float
    message: str