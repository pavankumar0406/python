import boto3

client = boto3.client('secretmanager')

response = client.create_secret(
    Name = 'MyDBsecrets',
    SecretString='{"username":"admin", "password":"password123"}'
)
