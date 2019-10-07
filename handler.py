import json


def hello(event, context):
    print ("event name is" + event)
    return 1

def createPost(event, context):
    print ("create post was called")
    return 1

def getuserinfo(event, context):
    print ("context is", context)
    # print ("id is "+ id)
    message = "This is the message"
    return {
        'statusCode' : 200,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps({'message' : message })
    }
