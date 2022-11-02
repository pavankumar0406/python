import boto3

client = boto3.client('secretmanager')

response = client.create_secret(
    Description='My test database secret created with the CLI',
    Name='MyTestDatabaseSecret',
    SecretString='{"username":"david","password":"EXAMPLE-PASSWORD"}',
)

print(response)
