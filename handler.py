import json
import boto3

def hello(event, context):
    print ("event name is" + event)
    return 1

def createPost(event, context):
    print ("create post was called")
    return 1

def getuserinfo(event, context):
    print ("context is", context)
   
    message = "Data was saved"
    return {
        'statusCode' : 200,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps({'message' : message })
    }

dynamodb = boto3.client('dynamodb')

def putuserinfo(event, context):
    dynamodb.put_item( TableName = 'posts',
        Item = {
            'username': '12345',
            'gameid':'123'
        }
    )
    message = "Data was saved"
    return {
        'statusCode' : 200,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps({'message' : message })
    }