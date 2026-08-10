import json
import boto3
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('Registration')


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
            'body': json.dumps(
                response['Items'],
                cls=DecimalEncoder
            )
        }

    except Exception as e:

        return {
            'statusCode': 500,
            'body': json.dumps({
                'message': str(e)
            })
        }