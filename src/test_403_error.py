
from unittest.mock import Mock
import requests


def handle_api_response(response):
    """Handle common API response status codes."""

    if response.status_code == 200:
        return "SUCCESS: API request completed successfully."

    elif response.status_code == 403:
        return (
            "ERROR 403: Forbidden - Access denied.\n"
            "Possible causes: Insufficient permissions or restricted API access.\n"
            "Solution: Check API permissions, authentication, and RLS policies."
        )

    else:
        return f"ERROR: HTTP Status {response.status_code}"


def test_403_error():
    # Simulate a server returning HTTP 403 Forbidden
    mock_response = Mock(spec=requests.Response)
    mock_response.status_code = 403

    result = handle_api_response(mock_response)

    print("=== HTTP 403 ERROR HANDLING TEST ===")
    print(result)

    assert "ERROR 403: Forbidden" in result
    print("\nTEST PASSED: HTTP 403 error handled correctly.")


if __name__ == "__main__":
    test_403_error()
