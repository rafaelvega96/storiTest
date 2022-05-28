
from functions.readS3 import readS3
from functions.calculateSummaryEmail import calculateSummary
from posix import environ
import os
import boto3
import json

bucket_s3_url = os.environ['BUCKET_S3_URL']
region_name = os.environ['REGION_NAME']


def action(event, context):
    try:
        # Read s3 to get the csv
        account_transaction = readS3(bucket_s3_url)
        print("account", account_transaction)
        # Calculate summary
        summary = calculateSummary(account_transaction)
        print("summary", summary)
        # Invoke lambda function to send a email
        lambda_client = boto3.client('lambda')
        lambda_payload = {"templateName": "StoriBalanceAccount",
                          "MailTo": ["rafaelvega96@hotmail.com"], "data": summary}
        payload_json = json.dumps(lambda_payload, indent=4)
        lambda_client.invoke(FunctionName='Stori-Send-Email',
                             InvocationType='RequestResponse',
                             Payload=payload_json)

        print("Proccess finished")

    except NameError as e:
        print(e)
