import json
import math
def lambda_handler(event, context):
    res = 0 
    for x in range(8**7,-1, -1):
        a = math.atan(x) * math.atan(x+1)*math.atan(x+2) 
        res = res + a
    return {
        'statusCode': 200
    }
