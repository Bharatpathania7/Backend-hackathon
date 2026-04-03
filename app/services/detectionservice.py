
DISTRESS_KEYWORDS = {
    "harassment": ["help", "bachao", "save me", "leave me", "mat chuo"],
    "health": ["chest pain", "heart attack", "saans", "breathing", "doctor"],
    "theft": ["chor", "steal", "robbery", "phone le gaya"],
    "accident": ["accident", "crash", "gir gaya", "injury", "blood"]
}


def detect_emergency_logic(text: str, volume: float, repeat_count: int):
    text_lower = text.lower()

    best_category = "normal"
    score = 0

    # 🔥 keyword detection
    for category, keywords in DISTRESS_KEYWORDS.items():
        for keyword in keywords:
            if keyword in text_lower:
                best_category = category
                score += 3

    # 🔥 strong panic phrases
    if "help help" in text_lower or "bachao bachao" in text_lower:
        score += 3

    # 🔥 volume boost
    if volume > 0.7:
        score += 2

    # 🔥 repetition boost (stronger)
    if repeat_count > 1:
        score += 2

    # 🔥 final decision
    emergency = score >= 5
    confidence = min(score / 8, 1.0)

    if not emergency:
        best_category = "normal"

    return emergency, best_category, confidence