
# AI Automation FYP — Limitations and Error Handling

**Project:** AI Automation System  
**Prepared by:** Sumavia Abid  
**Documentation Date:** 14 October 2026

## 1. Project Overview

This project integrates Supabase, Ollama, Python, Make.com, Zapier, and Google Sheets to automate data processing, AI analysis, and workflow execution.

## 2. System Limitations

### Supabase
- Database access requires valid credentials.
- Row Level Security (RLS) policies may restrict access.
- Internet connectivity is required.

### Ollama
- The AI model runs locally.
- Performance depends on system hardware.
- Ollama must be running before AI requests are processed.

### Make.com and Zapier
- Webhook URLs must be configured correctly.
- Automation execution depends on internet connectivity.
- Free plans and trials may impose usage limits.

### Google Sheets
- A valid Google account connection is required.
- Spreadsheet permissions must allow row creation.
- API quotas may limit large-scale automation.

## 3. HTTP Error Handling

| HTTP Code | Meaning | Recommended Action |
|---|---|---|
| 200 | Request successful | Confirm the expected result |
| 400 | Bad Request | Validate the request payload |
| 401 | Unauthorized | Verify authentication credentials |
| 403 | Forbidden | Check permissions, RLS policies, and API access |
| 404 | Not Found | Verify the endpoint URL |
| 429 | Too Many Requests | Apply rate limiting and retry with backoff |
| 500 | Server Error | Log the error and retry when appropriate |

## 4. Understanding HTTP 403 Forbidden

A 403 Forbidden response indicates that the server understood the request but refused to authorize the operation.

Possible causes include:
- Insufficient API permissions.
- Restricted database access.
- Incorrect Row Level Security policies.
- Disabled or unauthorized integrations.

Recommended troubleshooting:
1. Verify the API endpoint.
2. Check authentication and authorization settings.
3. Review Supabase RLS policies where applicable.
4. Inspect the HTTP response and application logs.
5. Retest after correcting the permission issue.

## 5. Security Considerations

- Store API keys and webhook URLs in the `.env` file.
- Exclude `.env` from GitHub using `.gitignore`.
- Never expose credentials in public documentation.
- Rotate compromised credentials and webhook URLs.
- Use the minimum permissions required.

## 6. Testing Status

- Supabase database integration: Completed.
- Ollama AI integration: Completed.
- Make.com to Google Sheets: Completed.
- Zapier to Google Sheets: Completed.
- HTTP 403 error handling: Simulated test completed successfully.

## 7. Conclusion

The AI Automation FYP demonstrates successful integration between Python, cloud automation platforms, AI processing, and Google Sheets.

Documenting system limitations and testing error-handling scenarios improves the reliability, maintainability, and security of the project.
## 8. HTTP 403 Error Handling Test Evidence

**Test Date:** 14 October 2026

**Test File:** src/test_403_error.py

**Test Type:** Simulated HTTP 403 Forbidden response

**Test Command:** python src/test_403_error.py

**Test Result:** PASSED

The Python test successfully detected a simulated HTTP 403
Forbidden response and displayed appropriate troubleshooting
guidance.

Note: This test validates simulated error-handling behavior.
Live API authorization failure testing was not performed.