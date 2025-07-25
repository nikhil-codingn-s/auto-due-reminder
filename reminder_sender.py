import pandas as pd
import boto3
import datetime
from email.utils import formatdate

# Load the Excel data
df = pd.read_excel("due_data.xlsx")

# Set AWS region and sender/receiver emails
AWS_REGION = "us-east-1"
SENDER_EMAIL = "tnnikhil36@gmail.com"  # Must be verified
RECIPIENT_EMAILS = [
    "nikhiltn401@gmail.com",
    "nikhiltn2004@gmail.com"
]  # All must be verified in sandbox

# Initialize boto3 client
ses = boto3.client('ses', region_name=AWS_REGION)

# Get today's date
today = datetime.date.today()

# Loop through each row
for index, row in df.iterrows():
    name = row["Name"]
    due_date = row["DueDate"]
    status = row["Status"]

    # Calculate delay
    days_late = (today - due_date.date()).days

    print(f"🔍 Checking {name} | Due: {due_date.date()} | Days Late: {days_late} | Status: {status}")

    # Condition to send reminder
    if status == "30day":
        # Email subject and body
        subject = f"⚠️ Payment Due Reminder for {name}"
        body = f"""Hi {name},

This is a friendly reminder that your payment was due on {due_date.date()} and is now {days_late} days overdue.

Please make the payment at the earliest to avoid further actions.

Thank you,
Auto Reminder System
"""

        # Send email to each recipient
        for recipient in RECIPIENT_EMAILS:
            try:
                print(f"📤 Sending email to {recipient}...")
                response = ses.send_email(
                    Source=SENDER_EMAIL,
                    Destination={'ToAddresses': [recipient]},
                    Message={
                        'Subject': {'Data': subject},
                        'Body': {
                            'Text': {'Data': body}
                        }
                    }
                )
                print(f"✅ Email sent to {recipient} | Message ID: {response['MessageId']}")
            except Exception as e:
                print(f"❌ Failed to send email to {recipient} | Error: {e}")

print("✅ Script finished.")

