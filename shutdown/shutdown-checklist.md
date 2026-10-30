
# Final Shutdown Checklist — AI Automation FYP

**Prepared by:** Sumavia Abid  
**Preparation Date:** 26 October 2026  
**Planned Shutdown Date:** 31 October 2026  
**Status:** Prepared — Execution Pending

## 1. Pre-Shutdown Verification
- [ ] Confirm all required project tasks are completed.
- [ ] Review regression test results and MVP support evidence.
- [ ] Obtain pending A12–A14 witness verification and sign-off.
- [x] Verify all required files are committed to GitHub.

## 2. Data Backup and Archival
- [ ] Export and securely archive required Supabase database records.
- [x] Verify backup files are readable and complete.
- [x] Archive final reports, test results, and documentation.
- [ ] Confirm archived data can be restored if required.
- Verification note (30 October 2026): Archived test_users_rows.csv was restored to a temporary location, matched the original byte-for-byte, and all 30 CSV records were verified. Full Supabase database restore verification remains pending.
- Schema verification (30 October 2026): All four archived schema files were found, readable, and non-empty. Full Supabase database backup and restore verification remain pending.
- CSV export verification (30 October 2026): Latest Supabase test_users export was archived locally and compared with the previous export using FC /B. Result: no differences encountered; 30 test-user records confirmed.
## 3. Integration Shutdown
- [ ] Stop active ngrok tunnels, if running.
- [ ] Disable unused automation workflows and webhooks.
- [ ] Confirm no active processes depend on these integrations.

## 4. Credential Security
- [ ] Revoke non-archival API keys and temporary access tokens.
- [ ] Rotate any credentials exposed during testing.
- [ ] Confirm `.env` and other secret files are excluded from GitHub.
- [ ] Never include actual API keys or passwords in evidence files.

## 5. Final Repository Verification
- [ ] Verify source code, documentation, and test evidence.
- [ ] Confirm GitHub repository is updated.
- [ ] Review `/shared/README.md` archival index.
- [ ] Record any unresolved external dependencies.

## 6. Final Confirmation
- [ ] Obtain required final approval.
- [ ] Post shutdown confirmation in the designated Slack channel.
- [ ] Record the shutdown completion date and final status.

## Outstanding Dependency
Affan's actual MVP test evidence for A12, A13, and A14 has not yet been received. Witness verification and final sign-off remain pending.

## Current Status
Checklist prepared. No services have been shut down and no API keys have been revoked as part of this checklist preparation.
