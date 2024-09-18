import boto3
from botocore.exceptions import ClientError
import json, random, requests
from datetime import datetime

def get_secret():
    secret_name = "openweathermap_api_key"
    region_name = "eu-north-1"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        # For a list of exceptions thrown, see
        # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
        raise e

    secret = get_secret_value_response['SecretString']

    return secret

ny_times_square_lat = 40.758896
ny_times_square_lon = -73.985130
API_key = get_secret()
print(API_key)
api_url = "https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={API_key}"

kinesis = boto3.client('kinesis', region_name='eu-north-1')


def get_api_data():
    pass

def put_to_kinesis():
    while True:
        data = 'baba'
        kinesis.put_record(
            StreamName='weather-data-stream',
            Data=json.dumps(data),
            PartitionKey='partition_key'
        )
        print(f"Put data: {data}")