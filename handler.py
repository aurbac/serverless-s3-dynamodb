import json
import boto3
import os

def hello(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    table_name = os.environ['tableName']

    print(json.dumps(event))

    dynamodb_client = boto3.client("dynamodb")

    for record in event['Records']:
        print(json.dumps(record))
        response = dynamodb_client.put_item(
            TableName=table_name,
            Item={
                'key_object': {
                    'S': record["s3"]["object"]["key"]
                },
                'bucket_name': {
                    'S': record["s3"]["bucket"]["name"]
                },
                'size_object': {
                    'N': str(record["s3"]["object"]["size"]),
                }
            }
        )

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
