
import os
import requests
from dotenv import load_dotenv

# Load environment variables securely
load_dotenv()

ZAPIER_WEBHOOK_URL = os.getenv("ZAPIER_WEBHOOK_URL")


def send_to_zapier(data):
    if not ZAPIER_WEBHOOK_URL:
        print("ERROR: ZAPIER_WEBHOOK_URL is missing in .env")
        return False

    try:
        response = requests.post(
            ZAPIER_WEBHOOK_URL,
            json=data,
            timeout=15
        )
        response.raise_for_status()

        print("SUCCESS: Data sent to Zapier!")
        print("HTTP Status:", response.status_code)
        return True

    except requests.RequestException as error:
        print("ERROR: Failed to send data to Zapier.")
        print("Details:", error)
        return False


if __name__ == "__main__":
    test_data = {
        "name": "Zapier Live Test User",
        "source": "Python Live Test",
        "status": "active"
    }

    send_to_zapier(test_data)
