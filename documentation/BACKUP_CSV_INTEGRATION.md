
# Backup CSV Integration — Implementation and Testing

**Project:** AI Automation FYP  
**Student:** Sumavia Abid  
**Module:** Backup Status CSV Data Processing and Automated Reporting  
**Testing Date:** 20 October 2026  
**Status:** Successfully Tested with Sample CSV Data

---

## 1. Introduction

The Backup CSV Integration module demonstrates automated backup monitoring and reporting using Python and structured CSV data.

The system reads backup records, analyzes backup statuses and types, calculates total backup duration, identifies failed backups, and generates a timestamped text report.

This module uses sample backup records rather than connecting to a live backup management platform.

## 2. Objectives

- Read and process backup records from a CSV file.
- Display backup information using a Python connector.
- Calculate status-wise backup summaries.
- Analyze full and incremental backup types.
- Calculate total backup duration.
- Identify failed backup operations.
- Generate an automated timestamped report.
- Maintain source code and documentation in GitHub.

## 3. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Data processing and automation |
| CSV | Structured backup records |
| pathlib | File and directory management |
| csv.DictReader | CSV data parsing |
| collections.Counter | Summary calculations |
| datetime | Report timestamps |
| VS Code | Development and testing |
| Git and GitHub | Version control and documentation |

## 4. Project File Structure

```text
ai-automation-project-main/
├── fixtures/
│   └── backup-status.csv
├── src/
│   ├── backup_connector.py
│   └── backup_report.py
├── reports/
│   └── backup_report_20261020_102539.txt
└── documentation/
    └── BACKUP_CSV_INTEGRATION.md
```

**Note:** Generated reports are stored locally and are not included in GitHub source-code commits.

## 5. CSV Dataset

**File:** `fixtures/backup-status.csv`

The CSV dataset contains eight sample backup records.

### CSV Fields

| Field | Description |
|---|---|
| backup_id | Unique backup identifier |
| system_name | Name of the system or database |
| backup_type | Full or Incremental |
| status | Success, Failed, or In Progress |
| backup_date | Backup execution date |
| duration_minutes | Backup duration in minutes |

### Sample Record

```csv
backup_id,system_name,backup_type,status,backup_date,duration_minutes
B001,CRM Database,Full,Success,2026-10-19,25
```

## 6. Backup Connector Implementation

**Python File:** `src/backup_connector.py`

The connector performs the following operations:

1. Locates the backup CSV dataset.
2. Opens and reads the CSV file.
3. Converts CSV rows into structured Python dictionaries.
4. Displays the total number of backup records.
5. Prints backup IDs, system names, types, statuses, dates, and durations.

### Execution Command

```bash
python src/backup_connector.py
```

### Testing Result

The connector successfully read and displayed all eight backup records.

**Result:** Passed

## 7. Automated Backup Report Implementation

**Python File:** `src/backup_report.py`

The reporting module:

1. Loads backup records from the CSV dataset.
2. Counts backup records by status.
3. Counts records by backup type.
4. Calculates total backup duration.
5. Identifies failed backup records.
6. Creates the reports directory if required.
7. Generates a timestamped text report.
8. Displays a summary in the terminal.

### Execution Command

```bash
python src/backup_report.py
```

### Generated Report

```text
reports/backup_report_20261020_102539.txt
```

## 8. Testing and Results

**Testing Date:** 20 October 2026

| Test Case | Expected Result | Actual Result | Status |
|---|---|---|---|
| CSV File Reading | Load 8 records | 8 records loaded | Passed |
| Connector Execution | Display backup details | Details displayed | Passed |
| Status Analysis | Calculate status totals | Totals calculated | Passed |
| Backup Type Analysis | Count backup types | Counts calculated | Passed |
| Duration Calculation | Calculate total duration | 179 minutes | Passed |
| Failed Backup Detection | Identify failed backups | 2 failed backups | Passed |
| Report Generation | Save timestamped report | Report saved | Passed |

### Verified Report Summary

| Metric | Result |
|---|---:|
| Total Backups | 8 |
| Successful Backups | 5 |
| Failed Backups | 2 |
| In Progress Backups | 1 |
| Full Backups | 4 |
| Incremental Backups | 4 |
| Total Backup Duration | 179 minutes |

### Terminal Output

```text
=== BACKUP REPORT GENERATED ===
Total Backups: 8
Successful: 5
Failed: 2
In Progress: 1
Report Saved: .../reports/backup_report_20261020_102539.txt
```

## 9. Limitations

- The module uses sample CSV data rather than a live backup platform.
- Backup records are processed locally.
- No real backup operation is triggered or restored.
- The system does not currently send automatic failure notifications.
- The report is a text file rather than an interactive dashboard.
- Generated reports are stored locally.

## 10. Conclusion

The Backup CSV Integration module was successfully implemented and tested using Python and eight sample backup records.

The system correctly calculated status-wise and type-wise summaries, identified failed backup operations, calculated a total backup duration of 179 minutes, and generated an automated timestamped report.

**Final Result: Backup CSV Data Processing and Automated Reporting Successfully Tested.**
