
import requests


class MakeConnector:
    def __init__(self, webhook_url=None):
        self.webhook_url = webhook_url

    def send_data(self, data):
        if not self.webhook_url:
            return {
                "limited_visibility": True,
                "entities": [],
                "message": "Make webhook URL is not configured"
            }

        try:
            response = requests.post(
                self.webhook_url,
                json=data,
                timeout=30
            )

            if response.status_code == 403:
                return {
                    "limited_visibility": True,
                    "entities": []
                }

            response.raise_for_status()

            return {
                "success": True,
                "status_code": response.status_code
            }

        except requests.exceptions.RequestException as error:
            return {
                "success": False,
                "error": str(error)
            }
