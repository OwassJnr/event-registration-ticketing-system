import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Registration')


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
            'body': json.dumps({
                'message': 'Registration cancelled'
            })
        }

    except Exception as e:

        return {
            'statusCode': 500,
            'body': json.dumps({
                'message': str(e)
            })
        }