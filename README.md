# 🔐 Automated Security Incident Response System (AWS)

## 📌 Overview

This project implements a **serverless security incident response system** on AWS that automatically detects suspicious IAM activity and responds in real time.

It simulates a basic **Security Operations Center (SOC) automation pipeline**, where AWS services work together to monitor, analyze, and respond to potential security threats.

---

## 🚨 Problem Statement

In cloud environments, malicious or accidental IAM actions (such as creating access keys or modifying policies) can lead to serious security breaches.

This system automates the detection and response process to reduce human delay and improve security posture.

---

## 🏗️ Architecture
<img width="2720" height="2000" alt="image" src="https://github.com/user-attachments/assets/d58b0c8a-f807-415d-bb04-285e82a20c1c" />

### Flow Description:

1. **AWS CloudTrail** logs all IAM and account activity  
2. **Amazon EventBridge** filters suspicious events  
3. **AWS Lambda** processes and analyzes events  
4. **Amazon SNS** sends real-time alerts  
5. **AWS IAM** automatically disables compromised access keys (optional response action)

---

## ☁️ AWS Services Used

- AWS CloudTrail – API activity logging  
- Amazon EventBridge – Event routing and filtering  
- AWS Lambda – Serverless automation logic  
- Amazon SNS – Security notifications  
- AWS IAM – Identity and access management  

---

## ⚙️ Features

- Real-time detection of suspicious IAM activity  
- Automated incident response workflow  
- Email alerting system for security events  
- Optional automatic deactivation of compromised access keys  
- Fully serverless and scalable architecture  

---

## 🚨 Detected Security Events

The system monitors and responds to:

- `CreateAccessKey`
- `AttachUserPolicy`
- `PutUserPolicy`
- `DeactivateMFADevice`

---

## 🧪 Testing the System

### Option 1: AWS Console

1. Create an IAM test user  
2. Generate an access key  
3. Observe CloudTrail event logging  
4. EventBridge triggers Lambda automatically  
5. SNS sends alert email  

---

### Option 2: AWS CLI

```bash
aws iam create-access-key --user-name test-user
```
This generates a CloudTrail event that triggers the security pipeline.

---

📂 Lambda Function Logic

The Lambda function performs:

* Event parsing
* Risk analysis
* SNS notification
* IAM access key deactivation (if risky event detected)

---

🔐 Security Considerations
* IAM permissions should follow least privilege principle
* SNS topic access should be restricted
* CloudTrail should be enabled across all regions
* Logs should be monitored using CloudWatch

---

📊 Skills Demonstrated
* Cloud security automation
* Event-driven architecture
* Serverless computing (AWS Lambda)
* Incident response design
* IAM security management
* Real-world SOC workflow simulation

---

🚀 Future Improvements
* Slack/Discord integration for alerts
* Integration with AWS GuardDuty
* Machine learning-based anomaly detection
* Centralized security dashboard (CloudWatch / QuickSight)
* Multi-account AWS security monitoring

---

👨‍💻 Author

Chigozie Nwanze
Cloud Engineer
