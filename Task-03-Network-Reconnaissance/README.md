# Task 03: Network Reconnaissance & Port Scanning Audit
Intern: Isha Hingmire | ID: RTA.CY.26.CAC.00313

## Tools Used
Nmap, Wireshark, Kali Linux

## Commands Executed
1. nmap -sn 192.168.1.0/24 (Host Discovery)
2. nmap -sV -sC -O -p- 192.168.1.10 (Full Scan)
3. Wireshark filter: tcp.port == 21

## Findings
- 21/tcp FTP vsftpd 2.3.4 - CRITICAL (CVE-2011-2523)
- 22/tcp SSH OpenSSH 4.7 - Medium
- 80/tcp HTTP Apache 2.2.8 - Medium
- 445/tcp SMB Samba 3.0.20 - HIGH

## Wireshark Analysis
Found FTP credentials in plaintext: msfadmin/msfadmin
Shows insecure protocol usage.

## Mitigation
- Use SFTP instead of FTP
- Update all services
- Close unused ports with firewall

## Ethical Note
Scan done on self-owned Metasploitable2 VM in isolated lab, not public network.

Proof: Lab environment Kali 2024.1
