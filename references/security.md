# Security-sensitive debugging

Use when a change affects authentication, authorization, secrets, untrusted input, or persistent data. A broader security audit is a separately scoped task.

- Establish the relevant trust boundary and threat: who controls the input, which operation is protected, and which data can be read or changed?
- Verify server-side authorization for the affected operation, including denied and cross-user/tenant cases when applicable. UI visibility is not an authorization check.
- Use context-appropriate output encoding and parameterized queries. Do not substitute a generic sanitizer or a CORS setting for access control.
- Avoid exposing secrets in logs, diagnostic cards, memory files, or test artifacts. Prefer redacted reproductions and fixtures.
- For persistence changes, consider data compatibility, failure handling, and recovery. Do not run destructive migrations or production probes outside the user's authorized scope.
- Use existing relevant scanners and tests where available; state their coverage and limits. A successful scan is evidence about those checks, not a claim of universal security.

Record actionable findings with evidence and scope. Keep unrelated vulnerabilities separate from a focused fix unless the user has authorized their remediation.
