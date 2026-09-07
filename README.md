🚀 AWS Lambda + S3 Trigger Project

📌 Project Overview

This project demonstrates an event-driven serverless architecture using AWS Lambda and Amazon S3.

Whenever a ".jpg" file is uploaded to an Amazon S3 bucket, an S3 event automatically triggers the AWS Lambda function. The Lambda function uses Python to read the S3 event details and log the bucket name and uploaded file name to Amazon CloudWatch Logs.

---

☁️ AWS Services Used

- Amazon S3 – Stores uploaded image files
- AWS Lambda – Processes the S3 event
- Amazon CloudWatch – Monitors Lambda execution and displays logs

---

🎯 Project Objective

To implement an event-driven file handling workflow using AWS serverless services by automatically triggering a Lambda function whenever a ".jpg" image is uploaded to an S3 bucket.

---

🏗️ Architecture Diagram

"AWS Lambda + S3 Architecture Diagram" (screenshots/Architecture-Diagram.jpeg)

---

🔧 Implementation Steps

Step 1: Create an S3 Bucket

1. Open the AWS Management Console.
2. Navigate to Amazon S3.
3. Click Create bucket.
4. Enter a unique bucket name.
5. Click Create bucket.

---

Step 2: Create a Lambda Function

1. Open AWS Lambda.
2. Click Create function.
3. Select Author from scratch.
4. Enter:
   - Function Name: "ImageProcessing"
   - Runtime: Python 3.x
5. Click Create function.

---

Step 3: Configure S3 Trigger

1. Open the Lambda function.
2. Click Add trigger.
3. Select Amazon S3.
4. Choose the created S3 bucket.
5. Select the event type:
   - Object Created (PUT)
6. Add a suffix filter:
   - ".jpg"
7. Click Add.

The suffix filter ensures that the Lambda function is triggered only when ".jpg" files are uploaded.

---

Step 4: Lambda Function Code

def lambda_handler(event, context):
    print("Image uploaded to S3")

    bucket_name = event['Records'][0]['s3']['bucket']['name']
    file_name = event['Records'][0]['s3']['object']['key']

    print(f"Bucket: {bucket_name}")
    print(f"File Uploaded: {file_name}")

    return {
        'statusCode': 200,
        'body': 'File processed successfully'
    }

Click Deploy after adding or updating the code.

---

Step 5: Test the Trigger

1. Open the configured S3 bucket.
2. Upload a file such as "image.jpg".
3. S3 automatically triggers the Lambda function.
4. Verify that the Lambda function executes successfully.

---

Step 6: Verify Execution

1. Open Amazon CloudWatch.
2. Navigate to the Lambda function's Log groups.
3. Open the latest log stream.
4. Verify the uploaded file details.

Example output:

Image uploaded to S3
Bucket: s3-trigger-image-bucket
File Uploaded: sunflower.jpg

---

📸 Screenshots

The following screenshots are included in the "screenshots" folder:

1. Architecture Diagram
2. S3 Bucket Creation
3. Lambda Function Creation
4. Lambda Function Code
5. S3 Trigger Configuration
6. Image Upload to S3
7. CloudWatch Logs Output

---

✅ Project Outcome

- Created an Amazon S3 bucket for image storage.
- Developed an AWS Lambda function using Python.
- Configured an S3 event trigger for ".jpg" files.
- Automatically triggered Lambda when an image was uploaded.
- Verified the Lambda execution through Amazon CloudWatch Logs.

---

👩‍💻 Author

Gummalla Alekya
B.Tech CSE Student | AWS & Cloud Enthusiast