import boto3

client = boto3.client('secretmanager')

response = client.create_secret(
    Name = 'My-DB-secrets',
    SecretString='{"username":"admin", "password":"password123"}'
)
