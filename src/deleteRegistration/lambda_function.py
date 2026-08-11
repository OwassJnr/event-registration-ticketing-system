import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Registration')

CORS_HEADERS = {
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Allow-Methods': 'GET,POST,DELETE,OPTIONS'
}


def lambda_handler(event, context):

    try:

        registration_id = event['pathParameters']['id']

        response = table.get_item(
            Key={
                'registrationId': registration_id
            }
        )

        if 'Item' not in response:

            return {
                'statusCode': 404,
                'headers': CORS_HEADERS,
                'body': json.dumps({
                    'message': 'Registration not found'
                })
            }

        table.delete_item(
            Key={
                'registrationId': registration_id
            }
        )

        return {
            'statusCode': 200,
            'headers': CORS_HEADERS,
            'body': json.dumps({
                'message': 'Registration cancelled'
            })
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