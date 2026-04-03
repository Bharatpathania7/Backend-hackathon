
from fastapi import APIRouter
from app.models.schemas import DetectRequest, DetectResponse
from app.services.detection_service import detect_emergency_logic
from app.services.twilio_service import send_sms, make_call

router = APIRouter()


@router.post("/detect-emergency", response_model=DetectResponse)
def detect_emergency(payload: DetectRequest):

    # Step 1: AI detection
    emergency, category, confidence = detect_emergency_logic(
        text=payload.text,
        volume=payload.volume,
        repeat_count=payload.repeat_count
    )

    # Step 2: If emergency → send SMS + CALL (ONLY if contacts exist)
    if emergency and payload.contacts:
        maps_link = f"https://maps.google.com/?q={payload.latitude},{payload.longitude}"

        sms_text = (
            f"🚨 Emergency detected!\n"
            f"Type: {category}\n"
            f"User ID: {payload.user_id}\n"
            f"Location: {maps_link}"
        )

        # 👉 LOOP safely
        for contact in payload.contacts:
            try:
                send_sms(contact, sms_text)
                make_call(contact)
            except Exception as e:
                print(f"❌ Failed for {contact}: {e}")

    # Step 3: Return response
    return DetectResponse(
        emergency=emergency,
        category=category,
        confidence=confidence,
        message="Emergency detected" if emergency else "No emergency detected"
    )