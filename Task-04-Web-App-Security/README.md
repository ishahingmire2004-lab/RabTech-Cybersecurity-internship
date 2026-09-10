# Task 04: Web Application Vulnerability Assessment (OWASP Top 10)
Intern: Isha Hingmire | ID: RTA.CY.26.CAC.00313
Target: OWASP Juice Shop http://localhost:3000 (Local Lab)

### Tools: Burp Suite, Chrome DevTools, Docker

### 1. SQL Injection (A03:2021)
Payload: ' OR '1'='1 --
Location: Login -> Email field
Result: Admin login bypass, authentication bypassed
Impact: Critical - DB compromise
Fix: Use prepared statements, parameterized queries

### 2. XSS - Cross Site Scripting (A03:2021)
Payload: <iframe src="javascript:alert('XSS by Isha')">
Location: Search bar / Feedback
Result: Stored XSS, alert popup executed
Impact: High - Session hijack, cookie theft
Fix: Output encoding, Input sanitization, CSP header

### 3. Broken Access Control / IDOR (A01:2021)
Test: Changed /rest/user/1 to /rest/user/2 via Burp Suite
Result: View other users data without permission
Impact: High - Data breach
Fix: Server side authorization checks

### Screenshots
- SQLi bypass screenshot
- XSS alert popup
- Burp intercept

### Ethical Note
Testing done on self-hosted OWASP Juice Shop v16.0.0 in isolated Docker, not live site, for education only.
