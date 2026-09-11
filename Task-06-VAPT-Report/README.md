# Task 06 - Comprehensive Penetration Testing Report & Capstone

**Intern:** Isha Hingmire | **ID:** RTA.CY.26C.AC.00313
**Internship:** RabTech Cybersecurity & Ethical Hacking (10 Sep - 10 Oct 2025)

## Objective
Compile all previous tasks (03,04,05) into a formal executive-ready VAPT report with CVSS 3.1, OWASP mapping, and remediation timeline.

## Risk Matrix

| ID | Vulnerability | Severity | CVSS | OWASP 2021 | Asset |
|---|---|---|---|---|---|
| V-01 | SQL Injection | Critical | 9.8 | A03 Injection | Task-04 |
| V-02 | Hardcoded AES Key | Critical | 9.1 | A02 Crypto Failures | Task-05 aes_256_gcm.py |
| V-03 | Open Ports 22,445 | High | 7.5 | A01 Broken Access | Task-03 |
| V-04 | Weak Password Hash MD5 | High | 7.4 | A02 Crypto Failures | Task-05 password_hashing.py |
| V-05 | Missing HSTS Headers | Medium | 5.3 | A05 Misconfig | Web App |
| V-06 | Insecure RSA PKCS1v15 | Medium | 5.9 | A02 Crypto Failures | Task-05 rsa_signature.py |

## Technical Findings Summary

**Task-03 Network:** Nmap scan found open ports. Fixed via firewall rules.
**Task-04 Web App:** ZAP/Burp found SQLi. Fixed via prepared statements.
**Task-05 Crypto:** 
- AES-256-GCM with random 12-byte nonce (secure)
- RSA 2048 PSS + SHA256 (secure)
- bcrypt with salt + work factor 12 (secure)
- Best Practice: ENV variables / Vault, Rotate AES 90 days, RSA 1 year

## Remediation Timeline

- **P0 Critical (7 Days):** Fix SQLi, Move keys to Vault
- **P1 High (15-30 Days):** Close port 445, Enforce bcrypt
- **P2 Medium (90 Days):** Add HSTS/CSP headers

## Expected Proof
1. Formal VAPT Report PDF (15-20 pages) - uploaded below
2. GitHub Security Lab Repo - This repo

**Status: COMPLETED - Ready for Mentor Review**
