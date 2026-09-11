# Task 06 - Comprehensive Penetration Testing Report & Capstone

**Intern:** Isha Hingmire | **ID:** RTA.CY.26C.AC.00313
**Repo:** RabTech-Cybersecurity-internship

### Objective
Synthesize security assessments into an enterprise-grade VAPT Report for executive committee.

### Implementation Steps (As per task)
- Compiled executive-ready VAPT report with executive summary, risk matrix (CVSS 3.1 scores), technical findings, and remediation timelines.
- Mapped vulnerabilities to CVSS scores and OWASP categories.
- Provided prioritized step-by-step patch guidelines for developers and sysadmins.
- Submitted final report for mentor review.

### Risk Matrix (CVSS 3.1 + OWASP)
| ID | Vulnerability | Severity | CVSS | OWASP | Asset |
|---|---|---|---|---|---|
| V-01 | SQL Injection in login | Critical | 9.8 | A03:2021-Injection | Task-04 |
| V-02 | Hardcoded AES Key | Critical | 9.1 | A02:2021-Crypto Failures | Task-05 aes_256_gcm.py |
| V-03 | Open Ports 22,445 | High | 7.5 | A01:2021-Broken Access | Task-03 |
| V-04 | Weak Password Storage MD5 | High | 7.4 | A02:2021-Crypto Failures | Task-05 password_hashing.py |
| V-05 | Missing HSTS Headers | Medium | 5.3 | A05:2021-Misconfig | Web App |
| V-06 | Insecure RSA Padding | Medium | 5.9 | A02:2021-Crypto Failures | Task-05 rsa_signature.py |

### Remediation Timeline
- **P0 Critical (7 Days):** Prepared Statements for SQLi, Move keys to ENV/Vault (AWS KMS / HashiCorp Vault)
- **P1 High (15-30 Days):** Firewall rules for ports, Enforce bcrypt cost 12 (Done in Task-05)
- **P2 Medium (90 Days):** Implement HSTS/CSP headers, Use RSA PSS + SHA256 only (Done in Task-05)

### Implementation Summary from Task-05
1. AES-256-GCM with random 12-byte nonce
2. RSA 2048 key pair + Digital Signature (PSS + SHA256)
3. bcrypt password hashing with salt + work factor 12
Best Practice: Never hardcode keys, Rotate AES every 90 days, RSA every 1 year.

### Expected Proof
✅ Formal Penetration Testing Report PDF (15-20 pages) - Attached as Task-06-VAPT-Report.docx
✅ GitHub Security Lab Repo - This repository

**Status: COMPLETED**
