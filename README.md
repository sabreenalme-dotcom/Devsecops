# DevSecOps Security Pipeline

Automated security gate for SENG 473 Information Security Final Project.

## Team Members
| Name | Student ID |
|------|------------|
| Fadumo Jamal Salad | 210208954 |
| Hafsa Omar Ismail Samatar | 210208735 |
| Sabreen Elmi Aidarus Gure | 210208856 |

## Demo Video
https://youtu.be/Au2ZEVvdwL8

## What It Does
Automatically scans code for security issues on every push and blocks deployment if vulnerabilities are found.

## Security Scans
- **Stage 1 - Gitleaks** → detects hardcoded secrets and API keys
- **Stage 2 - Bandit** → detects SQL injection and code vulnerabilities
- **Stage 3 - pip-audit** → detects vulnerable outdated libraries (44 CVEs found)

## Vulnerabilities Detected
| Type | Location | Tool |
|------|----------|------|
| Hardcoded secrets | app.py lines 7-9 | Gitleaks + Bandit |
| SQL Injection | app.py line 45 | Bandit |
| Outdated libraries | requirements.txt | pip-audit |

## How to Run
```bash
cd app
python app.py
