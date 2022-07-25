import os
import io
import boto3
import json
import csv

# grab environment variables
ENDPOINT_NAME = 'bytebankSDKEndpoint'
runtime= boto3.client('runtime.sagemaker')

def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    
    data = json.loads(json.dumps(event))
    payload = data['data']
    
    response = runtime.invoke_endpoint(EndpointName=ENDPOINT_NAME,
                                       ContentType='text/csv',
                                       Body=payload)
                                       
    result = json.loads(response['Body'].read().decode())

    
    pred = int(result)
    
    if pred == 0 : 
        msg = 'Não'
    else:
        msg = 'Sim'
    
    
    return msg