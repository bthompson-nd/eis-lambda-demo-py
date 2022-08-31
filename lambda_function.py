from lambda_types import LambdaDict, LambdaContext
import json

def lambda_handler(event: LambdaDict, context: LambdaContext) -> LambdaDict:
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
