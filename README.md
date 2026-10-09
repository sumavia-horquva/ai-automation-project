# AI Automation Project

## Project Overview

This project demonstrates an AI-powered automation system developed using Python, Supabase, Ollama, and GitHub.

The system retrieves user information from a Supabase database, processes the data using a locally running AI model, and automatically generates analytical reports.

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
│   ├── generate_report.py
│   ├── test_connection.py
│   ├── test_ai_database.py
│   └── test_ollama.py
├── reports/
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
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

## Conclusion

This project demonstrates the integration of cloud-based data storage, Python automation, and locally hosted artificial intelligence to build a functional AI-powered reporting system.