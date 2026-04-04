import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()


def send_sms(to_number: str, message: str):
    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    from_number = os.getenv("TWILIO_PHONE_NUMBER")

    if not account_sid or not auth_token or not from_number:
        raise ValueError("Twilio env variables missing")

    client = Client(account_sid, auth_token)


    return sms.sid
def make_call(to_number: str):
    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    from_number = os.getenv("TWILIO_PHONE_NUMBER")

    client = Client(account_sid, auth_token)

    call = client.calls.create(
        twiml="""
        <Response>
            <Say voice="alice">
                Emergency detected. Please check immediately. This is an automated alert from Smart Life Monitoring system. thankuh for contCTING Us
            </Say>
        </Response>
        """,
        from_=from_number,
        to=to_number
    )

    return call.sid