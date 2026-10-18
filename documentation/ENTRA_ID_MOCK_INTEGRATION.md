# Microsoft Entra ID Mock Integration — Implementation and Testing

**Project:** AI Automation FYP  
**Prepared By:** Sumavia Abid  
**Implementation Date:** 18 October 2026  
**Integration Type:** Simulated Microsoft Entra ID User Data

## 1. Project Overview

This module demonstrates how an AI automation system can process Microsoft Entra ID-style user information using a Python-based mock connector.

The implementation uses a local JSON dataset to simulate identity records without requiring live Microsoft Graph API access.

## 2. Objectives

- Create a mock Microsoft Entra ID user dataset.
- Retrieve user information using Python.
- Identify active and disabled user accounts.
- Generate an automated user status report.
- Validate the output through terminal execution.

## 3. Project Files

| File | Purpose |
|---|---|
| `fixtures/mock_entra.json` | Stores simulated Microsoft Entra ID user records |
| `src/entra_connector.py` | Reads and processes the mock identity dataset |
| `src/entra_user_report.py` | Generates the user status report |
| `reports/entra_user_report_20261018_075912.txt` | Generated report evidence |

## 4. Implementation Workflow

1. Create a structured JSON dataset containing user identity information.
2. Develop a Python connector to load the JSON records.
3. Extract relevant attributes, including display name, department, and account status.
4. Categorize users according to their `accountEnabled` value.
5. Generate a timestamped text report.
6. Verify the report output against the original dataset.

## 5. Testing Commands

**Test the mock connector:**

```bash
python src/entra_connector.py
```

**Generate the user report:**

```bash
python src/entra_user_report.py
```

## 6. Test Results

**Execution Status:** PASSED

| Metric | Result |
|---|---|
| Total Users | 3 |
| Active Users | 2 |
| Disabled Users | 1 |
| Report Generated | Yes |

### User Status Details

| User | Department | Account Status |
|---|---|---|
| Ali Khan | IT | Active |
| Sara Ahmed | Human Resources | Active |
| Ahmed Raza | Finance | Disabled |

The generated report correctly identified two active users and one disabled user.

## 7. Evidence

The successful execution was verified through:

- Python connector terminal output displaying three user records.
- Report generation terminal output confirming successful execution.
- Generated text report showing account status and user details.

## 8. Limitations

- This implementation uses simulated identity records.
- No live Microsoft Entra ID tenant is connected.
- Microsoft Graph API authentication has not been implemented.
- Real-time user synchronization has not been tested.
- Account creation, modification, and disabling operations are outside the current implementation scope.

## 9. Conclusion

The Microsoft Entra ID mock integration successfully demonstrates Python-based identity data retrieval, account status classification, and automated report generation.

The module provides a foundation for future integration with Microsoft Graph API and enterprise identity automation workflows.

**Final Result: Mock Integration and Report Generation Successfully Tested.**