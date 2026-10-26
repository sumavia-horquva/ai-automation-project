# Reset Procedure — AI Automation FYP

**Student:** Sumavia Abid
**Phase:** 1 — Reset Procedure
**Task Duration:** 25–27 October 2026

## Objective
Develop and test a repeatable reset procedure that
restores the AI Automation FYP test environment
to a known baseline state.

## Scope
- Identify baseline test data.
- Prepare a reset script.
- Restore approved test fixtures.
- Verify restored data against the baseline.
- Record execution results and screenshots.

## Safety
- Do not reset production databases.
- Do not delete existing project files.
- Do not expose credentials or API keys.
- Test the reset procedure using sample data only.

## Current Status

**Status: Successfully Completed and Verified**

**Verification Date:** 26 October 2026

### Reset Execution Results
- Baseline CSV files prepared successfully.
- Reset script executed successfully.
- Restored CSV files generated successfully.
- All 5 CSV files verified using Windows FC binary comparison.
- All comparisons returned: `FC: no differences encountered`.
- No production database or credentials were modified.

### Final Result
The reset procedure was successfully tested using sample CSV data.
All restored files match their baseline copies.