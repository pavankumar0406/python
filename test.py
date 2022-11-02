import boto3
from botocore.exceptions import ClientError


def get_secret():

    region_name = "ap-south-1"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
        )
    try: 
      response = client.create_secret(
    Name = 'MyDBsecrets',
    SecretString='{"username":"admin", "password":"password123"}'
    )

