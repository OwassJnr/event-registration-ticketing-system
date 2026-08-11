import json
import boto3
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('Registration')

CORS_HEADERS = {
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Allow-Methods': 'GET,POST,DELETE,OPTIONS'
}


class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return super().default(obj)


def lambda_handler(event, context):

    try:

        email = event['pathParameters']['email']

        response = table.query(
            IndexName='email-index',
            KeyConditionExpression=boto3.dynamodb.conditions.Key(
                'email'
            ).eq(email)
        )

        return {
            'statusCode': 200,
            'headers': CORS_HEADERS,
            'body': json.dumps(
                response['Items'],
                cls=DecimalEncoder
            )
        }

    except Exception as e:

        print("ERROR:", str(e))

        return {
            'statusCode': 500,
            'headers': CORS_HEADERS,
            'body': json.dumps({
                'message': str(e)
            })
        }