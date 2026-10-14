# Make.com Webhook and Google Sheets Integration

## AI Automation FYP — Integration Documentation

### 1. Project Overview

This integration demonstrates how a Python application can automatically send structured data to Make.com using a webhook and store the received information in Google Sheets.

The integration extends the AI Automation FYP by introducing a cloud-based, event-driven automation workflow.

### 2. Project Objectives

- Connect Python with Make.com using an HTTP webhook.
- Receive structured JSON data through a Make.com Custom Webhook.
- Automatically insert received data into Google Sheets.
- Map incoming JSON fields to spreadsheet columns.
- Validate the complete integration through practical testing.

### 3. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Send automation data |
| Requests Library | Make HTTP POST requests |
| Python-dotenv | Load environment variables |
| Make.com | Process incoming webhook events |
| Make.com Custom Webhook | Receive JSON payloads |
| Google Sheets | Store received records |
| Visual Studio Code | Development and testing |

### 4. System Architecture

The integration follows this workflow:

**Python Application → HTTP POST Request → Make.com Custom Webhook → Google Sheets Add a Row → Stored Record**

The Python application sends a JSON payload to the Make.com webhook endpoint. Make.com receives the payload and passes its values to the Google Sheets module, which creates a new spreadsheet row.

### 5. Python Webhook Connector

**File:** `src/make_connector.py`

A Python class named `MakeConnector` was implemented to send structured data to the Make.com webhook.

The connector uses the Requests library and supports:

- Configurable webhook URLs.
- JSON-based HTTP POST requests.
- HTTP response handling.
- A fallback message when the webhook URL is not configured.

The webhook endpoint is stored in the `.env` file using the `MAKE_WEBHOOK_URL` environment variable.

The actual webhook URL is excluded from public documentation and source control.