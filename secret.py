import boto3

client = boto3.client('secretmanager')

region_name = "ap-south-1"

response = client.create_secret(
    region_name=region_name,
    Name = 'MyDBsecrets',
    SecretString='{"username":"admin", "password":"password123"}'
)
