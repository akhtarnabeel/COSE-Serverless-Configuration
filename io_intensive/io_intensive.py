import json

def lambda_handler(event, context):

    for i in range(50000):
        f = open('my_file.txt', 'r')
        data = f.read()
        f.close()
    return {'statusCode': 200}
