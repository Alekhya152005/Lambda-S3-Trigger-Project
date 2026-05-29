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