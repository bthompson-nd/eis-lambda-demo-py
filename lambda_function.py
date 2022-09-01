'''The main Lambda module'''
import json
from lambda_types import LambdaDict, LambdaContext


def lambda_handler(event: LambdaDict, context: LambdaContext) -> LambdaDict:
    '''The main Lambda handler. The entry point for your logic.'''
    return {"statusCode": 200, "body": json.dumps(dict(event=event, context=context))}

