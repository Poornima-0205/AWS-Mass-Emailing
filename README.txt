 AWS Mass Emailing Using S3, Lambda and SES

:- Project Overview

This project demonstrates a serverless mass-emailing system using
Amazon S3, AWS Lambda, and Amazon SES.

The system automatically sends emails when a CSV file containing
recipient email addresses is uploaded to an Amazon S3 bucket.

:-Architecture

S3 → Lambda → SES → Email Recipients

:-AWS Services Used

- Amazon S3
- AWS Lambda
- Amazon SES
- Amazon CloudWatch
- AWS IAM

:- Project Workflow

1. A CSV file containing recipient email addresses is uploaded to an S3 bucket.
2. S3 generates an ObjectCreated event.
3. The event triggers the Lambda function.
4. Lambda reads the CSV file from S3.
5. Lambda extracts the recipient email addresses.
6. Lambda uses Amazon SES to send emails.
7. CloudWatch records Lambda execution logs.

:- CSV Format

The CSV file should contain an `email` column.

Example:

```text
email
example@gmail.com
example2@gmail.com