
import os
import vonage
# access required env vars
try:
    vonage_api_key = os.getenv("VONAGE_API_KEY")
    vonage_secret = os.getenv("VONAGE_SECRET")
    target_phone_number = os.getenv("TARGET_PHONE_NUMBER")

    # check if all required variables are present
    if not all([vonage_api_key, vonage_secret, target_phone_number]):
        raise ValueError("One or more required variable is missing")
except Exception as err:
    print(f"Environment variable missing: {err}")
    exit(1)

# initialize vonage client
client = vonage.Client(key=vonage_api_key, secret=vonage_secret)
sms = vonage.Sms(client)

# send message
response = sms.send_message(
    {
        "from": "VonageAPI",  # Replace with your sender ID or virtual number
        "to": target_phone_number,
        "text": "This is an SMS sent using the Vonage SMS API",
    }
)



# Success
{'message-count': '1', 'messages': [{'to': target_phone_number, 'message-id': '0418c4d7-0afb-4544-87e6-*', 'status': '0', 'remaining-balance': '1.70769000', 'message-price': '0.29231000', 'network': '621*'}]}

# Error
{'message-count': '1', 'messages': [{'status': '2', 'error-text': 'Missing api_key'}]}
