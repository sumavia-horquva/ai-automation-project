# AI Automation Project

## Project Overview
This project connects a Supabase database with a Python application and a locally running Ollama AI model to analyze test user records and generate text reports.

## Technologies Used
- Python
- Supabase
- Ollama AI
- Visual Studio Code
- Git and GitHub

## Workflow
1. Store 30 test user records in Supabase.
2. Connect Python to Supabase using configured credentials.
3. Retrieve test user names, roles, and statuses.
4. Send the retrieved data to the Ollama AI model for summarization.
5. Display the AI analysis in the terminal.
6. Save the analysis in a timestamped text file inside the reports folder.
7. Commit and push the updated Python code to GitHub.

## Verified Results
- Supabase API connection successful.
- 30 test users retrieved successfully.
- AI generated a summary of the user records.
- Timestamped AI analysis report created successfully.
- Updated source code pushed to the GitHub main branch.

## Security
The .env file contains local configuration and must not be committed to GitHub. Generated reports and virtual environment files are excluded using .gitignore.

## Conclusion
The working prototype demonstrates database retrieval, AI-assisted analysis, automated report generation, and source-code version control.