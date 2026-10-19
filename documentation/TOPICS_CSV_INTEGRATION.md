# Topics CSV Integration — Implementation and Testing

**Project:** AI Automation FYP  
**Student:** Sumavia Abid  
**Module:** Topics CSV Data Processing and Automated Reporting  
**Testing Date:** 19 October 2026  
**Status:** Successfully Tested with Sample CSV Data

## 1. Introduction

This module demonstrates automated topic management and reporting using Python and CSV data. The system reads structured topic records, analyzes their statuses, priorities, and categories, and generates a timestamped text report.

## 2. Objectives

- Load topic records from a CSV file.
- Extract topic IDs, names, categories, priorities, statuses, and assigned users.
- Calculate status-wise and priority-wise statistics.
- Generate an automated analysis report.
- Validate the output using sample data.

## 3. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Data processing and automation |
| CSV | Structured topic data storage |
| `csv.DictReader` | Reading CSV records |
| `collections.Counter` | Calculating summary statistics |
| `pathlib` | File and directory management |
| `datetime` | Timestamped report generation |
| GitHub | Version control and documentation |

## 4. Project Files

| File | Description |
|---|---|
| `fixtures/topics.csv` | Contains eight sample topic records |
| `src/topics_connector.py` | Reads and displays topic data |
| `src/topics_report.py` | Analyzes topics and generates reports |
| `reports/topics_report_20261019_124023.txt` | Generated test report (local output) |

## 5. Implementation Workflow

1. Create the sample topics CSV dataset.
2. Read the dataset using the Python CSV connector.
3. Validate topic information.
4. Analyze topic statuses, priorities, and categories.
5. Generate a timestamped text report.
6. Review the report for accuracy.

## 6. Testing Results

| Test | Expected Result | Actual Result |
|---|---|---|
| CSV loading | Read eight records | Passed |
| Topic extraction | Display topic details | Passed |
| Status analysis | Calculate status counts | Passed |
| Priority analysis | Calculate priority counts | Passed |
| Report generation | Save a text report | Passed |

### Verified Summary

| Metric | Result |
|---|---:|
| Total Topics | 8 |
| Active | 4 |
| In Progress | 2 |
| Completed | 2 |
| High Priority | 4 |
| Medium Priority | 3 |
| Low Priority | 1 |

## 7. Report Generation

The automated report was generated successfully on 19 October 2026.

**Output filename:** `topics_report_20261019_124023.txt`

The report includes status-wise, priority-wise, and category-wise summaries, followed by individual topic details.

## 8. Limitations

- This implementation uses locally stored sample CSV data.
- No live project-management API is connected.
- The current module generates text reports rather than an interactive dashboard.
- Generated reports are stored locally and are not part of the GitHub source-code deliverables.

## 9. Conclusion

The Topics CSV Integration module was successfully implemented and tested using Python. The system processed eight sample topics and generated an automated analysis report with accurate status and priority summaries.

**Final Result: Topics CSV Data Processing and Automated Reporting Successfully Tested.**