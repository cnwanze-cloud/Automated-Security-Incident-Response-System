# 🔐 Automated Security Incident Response System (AWS)

An event-driven, serverless Security Operations Center (SOC) automation system designed to monitor AWS infrastructure for high-risk IAM configuration changes or compromised credentials, dispatch real-time alerts, and execute automated remediation to enforce account security.

---

## 🏗️ Architecture Overview

The system uses an event-driven design to ensure sub-second response times between threat detection and mitigation, completely eliminating the need for manual intervention or persistent polling servers.

<img width="2720" height="2000" alt="architecture" src="https://github.com/user-attachments/assets/37b6a060-d35b-402d-bd97-d370549c1016" />

1. **Ingestion:** All account activity and API requests are captured by **AWS CloudTrail**.
2. **Filtering:** **Amazon EventBridge** monitors the CloudTrail log stream for specific high-risk API operations.
3. **Orchestration:** Upon matching a rule, EventBridge asynchronously triggers an **AWS Lambda** function containing the response logic.
4. **Notification:** The Lambda function extracts event metadata and publishes a critical notification payload to **Amazon SNS**, alerting the security team.
5. **Remediation:** Concurrently, Lambda interfaces with the **AWS IAM** API to instantly deactivate the compromised access keys.

---

## 🧰 Tech Stack & AWS Services

* **Cloud Platform:** Amazon Web Services (AWS)
* **Log Management:** AWS CloudTrail & Amazon S3
* **Event Broker:** Amazon EventBridge (CloudWatch Events)
* **Compute / Logic:** AWS Lambda (Python 3.x / Boto3)
* **Notification System:** Amazon SNS (Simple Notification Service)
* **Identity Management:** AWS IAM (Identity and Access Management)

---

## 🚨 Monitored Indicators of Compromise (IoCs)

The EventBridge rule is configured via an event pattern to target risky, administrative, or unauthorized account modifications:

```json
{
  "source": ["aws.iam"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventName": [
      "CreateAccessKey",
      "AttachUserPolicy",
      "PutUserPolicy",
      "DeactivateMFADevice"
    ]
  }
}
```

---

## 🛠️ Deployment & Configuration Guide

### Step 1: Enable Account-Wide Auditing
1. Navigate to the **AWS CloudTrail** console and select **Create Trail**.
2. Configure the following parameters:
   * **Trail name:** `security-trail`
   * **Apply to all regions:** Enabled (`True`)
   * **Storage:** Create a new S3 bucket (e.g., `security-logs-bucket-[UNIQUE_ID]`)
   * **Log events:** Management events (`Read` + `Write`)

### Step 2: Establish the Alerting Topology
1. Open the **Amazon SNS** console and create a new **Standard Topic** named `security-alerts`.
2. Copy the generated **Topic ARN** for subsequent environment configuration.
3. Create a **Subscription** within the topic:
   * **Protocol:** `Email`
   * **Endpoint:** `your-security-team-email@domain.com`
4. Confirm the subscription via the automated verification email sent to your inbox.

### Step 3: Configure the Least-Privilege Execution Role
1. Navigate to **IAM** ➔ **Roles** ➔ **Create Role** and select **Lambda** as the trusted entity.
2. Attach permissions following a zero-trust model:
   * `AWSLambdaBasicExecutionRole` (for CloudWatch logging)
   * A scoped inline policy granting `sns:Publish` for your specific topic ARN, and `iam:ListAccessKeys` / `iam:UpdateAccessKey` to allow account-wide credential isolation.
3. Name the role `SecurityIncidentLambdaRole`.

### Step 4: Deploy the Serverless Response Engine
1. Create a new **AWS Lambda** function named `SecurityIncidentResponder`.
2. Set the runtime to **Python 3.x** and select the existing execution role created in Step 3.
3. Deploy the core automated response logic provided in the `/src` directory of this repository (ensure you replace `YOUR_SNS_TOPIC_ARN` with your actual SNS ARN).

### Step 5: Wire the Event Pipeline
1. Open **Amazon EventBridge** and select **Rules** ➔ **Create Rule**.
2. Define the rule name as `security-incident-rule` and set the event source to **AWS events**.
3. Paste the JSON pattern defined in the *Monitored Indicators of Compromise* section.
4. Set the Target routing engine to point directly to the `SecurityIncidentResponder` Lambda function.

---

## 🧪 Validation & Testing Framework

To safely simulate an adversarial credential creation event, execute the following command via the AWS CLI using a non-root administrative identity:

```bash
aws iam create-access-key --user-name test-user
```

---

### Verification

1. **Detection**: CloudTrail captured the risky API call.
<img width="974" height="526" alt="image" src="https://github.com/user-attachments/assets/9984eefe-f6b4-4c61-8ed2-acd75066ab74" />

2. **Alerting**: The security team immediately received an SNS alert detailing the compromise.
<img width="974" height="526" alt="image" src="https://github.com/user-attachments/assets/85c49bd5-d4ff-44ac-bd06-6c376cae52e4" />
