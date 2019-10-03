import json


def hello(event, context):
    print ("event name is" + event)
    return 1

def createPost(event, context):
    print ("create post was called")
    return 1