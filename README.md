# AI Automation Project

## Project Overview

This project demonstrates an AI-powered automation system developed using Python, Supabase, Ollama, and GitHub.

The system retrieves user information from a Supabase database, processes the data using a locally running AI model, and automatically generates analytical reports.

The project also integrates Make.com webhooks with Google Sheets to enable event-driven automation. A Python connector sends structured JSON data to a Make.com webhook, which automatically adds the received information as a new row in Google Sheets.

## Project Objectives

- Connect a Python application to a cloud database.
- Retrieve and analyze user records.
- Integrate a local Large Language Model (LLM).
- Automate AI-powered report generation.
- Maintain project source code using Git and GitHub.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend development and automation |
| Supabase | PostgreSQL database and API |
| Ollama | Local AI model execution |
| Llama 3.2 | AI-based text analysis |
| Git | Version control |
| GitHub | Source code hosting |
| VS Code | Development environment |

## System Workflow

1. The Python application connects to Supabase.
2. User records are retrieved from the database.
3. Python prepares the data for analysis.
4. Ollama processes the information using Llama 3.2.
5. The application generates an AI-assisted summary.
6. A text report is saved in the `reports/` directory.

## Project Structure

```text
ai-automation-project/
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── database.py
│   ├── main.py
│   ├── ollama_connector.py
│   ├── make_connector.py
│   ├── entra_connector.py
│   ├── entra_user_report.py
│   ├── generate_report.py
│   └── slack_connector.py
├── fixtures/
│   ├── mock_entra.json
│   └── mock_slack.json
├── documentation/
│   ├── AI_AUTOMATION_WORKFLOW.md
│   ├── ENTRA_ID_MOCK_INTEGRATION.md
│   ├── MAKE_GOOGLE_SHEETS_INTEGRATION.md
│   ├── OLLAMA_CONNECTOR_TESTING.md
│   ├── SLACK_MOCK_INTEGRATION.md
│   ├── LIMITATIONS.md
│   └── AI_Automation_FYP_Evidence_Report.pdf
├── reports/
├── .env.example
├── .gitignore
├── README.md
└── requirements.txt
```

## Installation and Setup

1. Clone the GitHub repository.
2. Create a Python virtual environment.
3. Install the dependencies using `pip install -r requirements.txt`.
4. Configure Supabase credentials in a local `.env` file.
5. Install Ollama and download the `llama3.2:1b` model.
6. Run the database connection and AI integration tests.

## Testing

The following components have been tested:

- Supabase database connectivity.
- User record retrieval.
- Ollama local model execution.
- Python-to-Ollama API communication.
- AI analysis of Supabase data.
- Automated text report generation.

## Current Results

The application successfully retrieved 30 test-user records and generated an AI-assisted report.

The generated report included:

- Total users: 30
- Tester role: 30 users (100%)
- Active status: 30 users (100%)
- AI-generated summary of the user dataset

## Security

Database credentials are stored in a local `.env` file, which is excluded from Git version control.

The `.env.example` file serves as a configuration template without exposing actual credentials.

## Future Enhancements

- Build an interactive dashboard.
- Add automated scheduling.
- Support additional database tables.
- Improve AI-generated insights.
- Export reports in additional formats.

## Slack Mock Integration

The AI Automation FYP includes a Slack mock data integration module developed using Python and JSON.

### Implementation Details

- **Data Source:** Locally stored Slack-style JSON test data.
- **Mock Dataset:** 4 simulated Slack messages.
- **Python Connector:** `src/slack_connector.py`
- **JSON Fixture:** `fixtures/mock_slack.json`
- **Testing Date:** 18 October 2026
- **Status:** Successfully implemented and tested with mock data.

### Features Implemented

- Load simulated Slack messages from a JSON file.
- Process channel and message information.
- Display usernames, message content, and timestamps.
- Calculate the total number of messages.
- Handle missing mock data files.

### Test Results

The Python connector successfully processed and displayed 4 simulated Slack messages.

**Result:** Slack mock data integration test completed successfully.

### Documentation

[View Slack Mock Integration Documentation](documentation/SLACK_MOCK_INTEGRATION.md)

### Limitations

This module uses local JSON test data. Live Slack API connectivity, real-time synchronization, and message sending are not implemented.

## Conclusion

This project demonstrates the integration of cloud-based data storage, Python automation, and locally hosted artificial intelligence to build a functional AI-powered reporting system.


## CSV Data Processing and Automated Reporting

The project includes three Python-based CSV processing modules, successfully tested on 19 October 2026 using sample datasets.

### Sales CSV Integration
Processes sales transactions, calculates total sales revenue, analyzes payment statuses, and generates automated reports.

[View Sales CSV Documentation](documentation/SALES_CSV_INTEGRATION.md)

### Topics CSV Integration
Processes topic records, analyzes statuses, priorities, and categories, and generates automated summary reports.

[View Topics CSV Documentation](documentation/TOPICS_CSV_INTEGRATION.md)

### Leads CSV Integration
Processes lead records, analyzes lead statuses, sources, and priorities, and generates automated lead analysis reports.

[View Leads CSV Documentation](documentation/LEADS_CSV_INTEGRATION.md)

**Testing Status:** All three modules successfully tested with sample CSV data.


### Backup CSV Integration

Processes backup records, analyzes backup statuses and types,
identifies failed backups, and generates automated reports.

[View Backup CSV Documentation](documentation/BACKUP_CSV_INTEGRATION.md)

### Finance CSV Integration

Processes financial transactions, calculates confirmed income,
expenses, and net balance, and generates automated financial reports.

[View Finance CSV Documentation](documentation/FINANCE_CSV_INTEGRATION.md)

**CSV Testing Status:** All five CSV modules successfully tested
with sample data.
