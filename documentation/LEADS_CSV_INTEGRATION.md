# Leads CSV Integration — Implementation and Testing

**Project:** AI Automation FYP  
**Student:** Sumavia Abid  
**Module:** Leads CSV Data Processing and Automated Reporting  
**Testing Date:** 19 October 2026  
**Status:** Successfully Tested with Sample CSV Data

---

## 1. Introduction

The Leads CSV Integration module is designed to demonstrate automated lead data processing using Python and structured CSV files.

The module reads lead information, extracts relevant details, analyzes lead statuses, sources, and priorities, and generates a timestamped text report.

This implementation provides a foundation for lead management and reporting automation.

## 2. Objectives

The primary objectives of this module are:

1. Read structured lead records from a CSV file.
2. Extract lead information using Python.
3. Calculate the total number of leads.
4. Analyze leads based on their status.
5. Identify lead acquisition sources.
6. Generate priority-wise summaries.
7. Automatically generate a structured text report.
8. Validate the results through local testing.

## 3. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Data processing and report generation |
| CSV | Structured lead data storage |
| csv.DictReader | Reading CSV records |
| pathlib | File and directory management |
| collections.Counter | Lead statistics and summaries |
| datetime | Timestamped report generation |
| VS Code | Development and testing |
| GitHub | Source code version control and documentation |

## 4. Project File Structure

```text
ai-automation-project-main/
├── fixtures/
│   └── leads-2026-10-08.csv
├── src/
│   ├── leads_connector.py
│   └── leads_report.py
├── reports/
│   └── leads_report_20261019_124713.txt
└── documentation/
    └── LEADS_CSV_INTEGRATION.md
```

**Note:** Generated reports are stored locally and are excluded from GitHub source-code tracking.

## 5. Sample Dataset

The testing dataset contains eight fictional lead records.

Each record includes the following fields:

| Field | Description |
|---|---|
| lead_id | Unique lead identifier |
| lead_name | Name of the lead |
| email | Lead email address |
| source | Lead acquisition channel |
| status | Current lead status |
| priority | Lead priority level |
| assigned_to | Assigned team member |

**Dataset Location:** `fixtures/leads-2026-10-08.csv`

## 6. Implementation

### 6.1 Leads CSV Connector

**File:** `src/leads_connector.py`

The connector uses Python's built-in CSV library to read structured lead records.

Its main function, `get_leads_data()`, loads the CSV file and returns the records as a list of dictionaries.

The connector displays lead information including:

- Lead ID and name
- Email address
- Acquisition source
- Lead status
- Priority
- Assigned team member

**Testing Command:**

```bash
python src/leads_connector.py
```

**Testing Result:** Eight sample lead records were successfully processed and displayed in the VS Code terminal.

### 6.2 Automated Leads Report Generator

**File:** `src/leads_report.py`

The report generator imports the lead records from the connector and performs automated data analysis.

The implementation uses `collections.Counter` to calculate status-wise, source-wise, and priority-wise summaries.

The results are written to a timestamped text report.

**Testing Command:**

```bash
python src/leads_report.py
```

## 7. Testing and Results

**Testing Date:** 19 October 2026

The automated report generator executed successfully.

### 7.1 Lead Status Summary

| Status | Number of Leads |
|---|---:|
| New | 2 |
| Contacted | 2 |
| Qualified | 2 |
| Converted | 2 |
| **Total** | **8** |

### 7.2 Lead Source Summary

| Source | Number of Leads |
|---|---:|
| Website | 2 |
| Facebook | 1 |
| Google Ads | 1 |
| Referral | 2 |
| Instagram | 1 |
| LinkedIn | 1 |
| **Total** | **8** |

### 7.3 Lead Priority Summary

| Priority | Number of Leads |
|---|---:|
| High | 4 |
| Medium | 3 |
| Low | 1 |
| **Total** | **8** |

### 7.4 Terminal Output

```text
=== LEADS REPORT GENERATED ===
Total Leads: 8
New Leads: 2
Contacted Leads: 2
Qualified Leads: 2
Converted Leads: 2
Report Saved: .../reports/leads_report_20261019_124713.txt
```

**Result:** The program processed all eight sample leads and successfully generated the report.

## 8. Automated Workflow

The module follows this processing sequence:

```text
Sample Leads CSV File
          |
          v
Python Leads Connector
          |
          v
Read and Extract Lead Records
          |
          v
Lead Data Analysis
          |
          +--> Status-wise Summary
          |
          +--> Source-wise Summary
          |
          +--> Priority-wise Summary
          |
          v
Automated Report Generator
          |
          v
Timestamped Text Report
          |
          v
Local Reports Folder
```

## 9. Limitations

- The module uses a local CSV file rather than a live CRM connection.
- Real-time lead synchronization is not implemented.
- Lead creation and modification are outside the current scope.
- Email notifications and automatic lead assignment are not implemented.
- Reports are generated as text files rather than interactive dashboards.
- The module currently demonstrates local data processing and reporting, not a production CRM integration.

## 10. Conclusion

The Leads CSV Integration module was successfully implemented and tested using Python and sample CSV data.

The system processed eight lead records, calculated accurate status-wise, source-wise, and priority-wise summaries, and generated an automated timestamped report.

**Final Result: Leads CSV Data Processing and Automated Reporting Successfully Tested.**