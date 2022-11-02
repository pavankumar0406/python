import boto3

client = boto3.client('secretsmanager')

response = client.create_secret(
    region_name="ap-south-1",
    Name = 'MyDBsecrets',
    SecretString='{"username":"admin", "password":"password123"}'
)
