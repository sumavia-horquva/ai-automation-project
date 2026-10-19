# Jira Mock Integration — Implementation and Testing

**Project:** AI Automation FYP  
**Student:** Sumavia Abid  
**Module:** Jira Mock Data Integration  
**Testing Date:** 19 October 2026  
**Status:** Successfully Tested with Mock Data

## 1. Introduction

This module demonstrates how the AI Automation FYP processes Jira-style project issues using Python and locally stored JSON data.

## 2. Objective

The objective is to retrieve simulated Jira issues, analyze their statuses, and automatically generate a structured report.

## 3. Technologies Used

- Python
- JSON
- Visual Studio Code
- Git and GitHub

## 4. Project Files

| File | Purpose |
|---|---|
| `fixtures/mock_jira.json` | Stores simulated Jira issues |
| `src/jira_connector.py` | Reads and processes Jira issues |
| `src/jira_report.py` | Generates an automated issue report |
| `reports/jira_report_*.txt` | Locally generated report output |

## 5. Implementation

The Jira mock integration was implemented in the following stages:

1. Created a JSON dataset containing four Jira-style issues.
2. Developed a Python connector to retrieve the issues.
3. Tested issue retrieval through the VS Code terminal.
4. Developed an automated report-generation script.
5. Generated a timestamped report containing issue statistics.

## 6. Testing Commands

**Jira Connector Testing:**

```bash
python src/jira_connector.py
```

**Jira Report Generation:**

```bash
python src/jira_report.py
```

## 7. Test Results

| Metric | Result |
|---|---:|
| Total Issues | 4 |
| Done | 2 |
| In Progress | 1 |
| To Do | 1 |

**Result:** The Jira mock connector successfully retrieved four issues, and the report-generation script saved the issue summary to a text file.

## 8. Limitations

- This implementation uses locally stored mock JSON data.
- Live Jira API connectivity is not implemented.
- Real-time issue synchronization is not supported.
- Issue creation and modification in Jira are outside the current scope.

## 9. Conclusion

The Jira mock data integration was successfully implemented and tested using Python and JSON. The module demonstrates issue retrieval, status analysis, and automated report generation.

**Final Result: Jira Mock Data Integration Successfully Tested.**