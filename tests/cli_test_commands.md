# 📄 AWS CLI Test Commands

---

## 📌 Purpose
This document contains the AWS CLI commands used to validate the Security Incident Response System.

---

## ⚙️ Prerequisites

```bash
aws configure
```

---

🧪 IAM Test Actions

1. List IAM users
```bash
aws iam list-users
```

---

2. Create test user
```bash
aws iam create-user --user-name test-user
```

---

3. Create access key (triggers security pipeline)
```bash
aws iam create-access-key --user-name test-user
```

---
