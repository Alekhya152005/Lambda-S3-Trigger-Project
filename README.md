# 🚀 AWS Lambda + S3 Trigger Project

## 📌 Project Overview

This project demonstrates an event-driven serverless architecture using AWS Lambda and Amazon S3.

Whenever a `.jpg` file is uploaded to an Amazon S3 bucket, AWS Lambda is automatically triggered and executes Python code to process the event.

---

## ☁️ AWS Services Used

* Amazon S3
* AWS Lambda
* Amazon CloudWatch

---

## 🎯 Project Objective

To automate file processing using AWS serverless services by triggering a Lambda function whenever an image is uploaded to an S3 bucket.

---

## 🏗️ Architecture Diagram


User Uploads image.jpg
          │
          ▼
    Amazon S3 Bucket
          │
   Object Created Event
          │
          ▼
      AWS Lambda
          │
          ▼
   CloudWatch Logs


---

## 🔧 Implementation Steps

### Step 1: Create an S3 Bucket

1. Open AWS Management Console.
2. Navigate to Amazon S3.
3. Click **Create Bucket**.
4. Enter a unique bucket name.
5. Click **Create Bucket**.

---

### Step 2: Create a Lambda Function

1. Open AWS Lambda.
2. Click **Create Function**.
3. Select **Author from Scratch**.
4. Enter:

   * Function Name: `ImageProcessing`
   * Runtime: `Python 3.x`
5. Click **Create Function**.

---

### Step 3: Configure S3 Trigger

1. Open the Lambda function.
2. Click **Add Trigger**.
3. Select **Amazon S3**.
4. Choose the created bucket.
5. Select Event Type:

   * **PUT (Object Created)**
6. Add suffix filter:

   * `.jpg`
7. Click **Add**.

---

### Step 4: Lambda Function Code

```python
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
```

Deploy the function after adding the code.

---

### Step 5: Test the Trigger

1. Open the S3 bucket.
2. Upload a file named `image.jpg`.
3. Verify that the Lambda function is triggered automatically.

---

### Step 6: Verify Execution

1. Open Amazon CloudWatch.
2. Navigate to Logs.
3. Check the Lambda log stream.
4. Verify that the uploaded file details are displayed.

---

## 📊 Workflow


User
 │
 ▼
Upload image.jpg
 │
 ▼
Amazon S3 Bucket
 │
 ▼
Object Created Event
 │
 ▼
AWS Lambda Triggered
 │
 ▼
Process File
 │
 ▼
CloudWatch Logs Generated


---

## 📸 Screenshots

The following screenshots are available in the `screenshots` folder:

* S3 Bucket Creation
* Lambda Function Creation
* S3 Trigger Configuration
* Lambda Function Code
* Image Upload to S3
* CloudWatch Logs Output

---

## ✅ Project Outcome

* Created an Amazon S3 bucket.
* Developed a Lambda function using Python.
* Configured an S3 event trigger.
* Automated Lambda execution upon file upload.
* Verified execution through CloudWatch Logs.

---

## 👩‍💻 Author

**Gummalla Alekya**
B.Tech – Computer Science Engineering
Cloud Enthusiast ☁️ | AWS Learner 
