# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 3.1.x   | :white_check_mark: |
| < 3.0   | :x:                |

## Reporting a Vulnerability

We take the security of ks-eye seriously. If you discover a security vulnerability, please follow these steps:

### How to Report

1. **DO NOT** open a public GitHub issue
2. Email us at: kashsightplatform@gmail.com
3. Include:
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested fix (if any)

### What to Expect

- **Acknowledgment**: Within 48 hours
- **Initial assessment**: Within 5 business days
- **Fix timeline**: Depends on severity, typically within 30 days

### Security Considerations

#### Data Privacy

- All research data is stored locally in `data/research_history/`
- No data is transmitted to external servers without explicit user action
- AI queries go through `tgpt` which handles its own privacy

#### API Keys

- ks-eye does not store API keys directly
- AI provider configuration is in `data/config/agent_providers.json`
- Users should not commit configuration files with sensitive data

#### Dependencies

- We monitor dependencies for known vulnerabilities
- `pip audit` should be run periodically
- Update dependencies promptly when security fixes are released

### Best Practices for Contributors

1. **Never commit secrets** — Use environment variables or secure storage
2. **Validate all input** — Especially file paths and user-provided data
3. **Use safe file operations** — Avoid `eval()`, `exec()`, shell injection
4. **Review dependencies** — Check for known vulnerabilities before adding
5. **Follow principle of least privilege** — Request only necessary permissions

### Security Checklist for PRs

- [ ] No hardcoded secrets or API keys
- [ ] Input validation for all user-provided data
- [ ] Safe file path handling (no directory traversal)
- [ ] No shell command injection vulnerabilities
- [ ] Dependencies are up to date and secure
- [ ] Error messages don't leak sensitive information

---

Thank you for helping keep ks-eye secure! 🔒
