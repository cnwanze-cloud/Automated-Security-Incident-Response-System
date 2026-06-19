import json
import boto3

sns = boto3.client('sns')
iam = boto3.client('iam')

SNS_TOPIC_ARN = "arn:aws:sns:us-east-1:021655151277:security-alerts"

def lambda_handler(event, context):

    print("EVENT RECEIVED:", json.dumps(event))

    detail = event.get("detail", {})
    event_name = detail.get("eventName", "")
    user = detail.get("userIdentity", {}).get("userName", "unknown")

    # 1. ANALYZE EVENT
    risk_events = [
        "CreateAccessKey",
        "AttachUserPolicy",
        "PutUserPolicy",
        "DeactivateMFADevice"
    ]

    if event_name in risk_events:

        message = f"""
        SECURITY ALERT 🚨

        Suspicious Activity Detected:
        Event: {event_name}
        User: {user}

        Action required immediately.
        """

        # 2. SEND ALERT
        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Message=message,
            Subject="AWS Security Incident Alert"
        )

        # 3. AUTO-RESPONSE (DISABLE USER ACCESS KEY - OPTIONAL)
        try:
            access_keys = iam.list_access_keys(UserName=user)

            for key in access_keys['AccessKeyMetadata']:
                iam.update_access_key(
                    UserName=user,
                    AccessKeyId=key['AccessKeyId'],
                    Status='Inactive'
                )

        except Exception as e:
            print("Could not disable key:", str(e))

    return {
        "statusCode": 200,
        "body": json.dumps("Processed")
    }