# 📬 Amazon SNS Setup Notes (Security Incident Response System)

## 📌 Overview

This document describes the configuration of Amazon SNS used in the Automated Security Incident Response System.

Amazon SNS (Simple Notification Service) is used to send **real-time security alerts** to the security team when suspicious IAM activity is detected.

---

## 🎯 Purpose in This Project

SNS is responsible for:

- Sending immediate alerts when a security event is detected
- Notifying administrators of IAM-related suspicious activity
- Acting as the communication layer between Lambda and security personnel

---

## ⚙️ SNS Topic Configuration

### Topic Name:
security-alerts


### Region:

us-east-1 (or your selected region)


### Topic Type:

Standard Topic


---

## 📧 Subscription Setup

### Protocol:

Email


### Endpoint:

your-email@example.com


### Confirmation:
- AWS sends a confirmation email
- Subscription must be confirmed before receiving alerts

---

## 🔐 IAM Permissions

To allow Lambda to publish messages to SNS, the following permission is required:

```json
{
"Effect": "Allow",
"Action": "sns:Publish",
"Resource": "*"
}
```
