import json
import boto3
import uuid
from datetime import datetime

dynamodb = boto3.resource('dynamodb')

events_table = dynamodb.Table('Events')
registrations_table = dynamodb.Table('Registration')

CORS_HEADERS = {
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Allow-Methods': 'GET,POST,DELETE,OPTIONS'
}


def lambda_handler(event, context):

    try:

        # Log incoming request
        print("Incoming event:", json.dumps(event))

        body = json.loads(event.get('body', '{}'))

        event_id = body.get('eventId')
        name = body.get('name')
        email = body.get('email')

        print(f"Registration request received for {email}")

        # Validation
        if not event_id or not name or not email:

            return {
                'statusCode': 400,
                'headers': CORS_HEADERS,
                'body': json.dumps({
                    'message': 'Missing required fields'
                })
            }

        # Check event exists
        event_response = events_table.get_item(
            Key={'eventId': event_id}
        )

        if 'Item' not in event_response:

            return {
                'statusCode': 404,
                'headers': CORS_HEADERS,
                'body': json.dumps({
                    'message': 'Event not found'
                })
            }

        registration_id = str(uuid.uuid4())

        registration = {
            'registrationId': registration_id,
            'eventId': event_id,
            'name': name,
            'email': email,
            'timestamp': datetime.utcnow().isoformat()
        }

        print(f"Saving registration for event {event_id}")

        registrations_table.put_item(
            Item=registration
        )

        print(f"Registration successful: {registration_id}")

        return {
            'statusCode': 201,
            'headers': CORS_HEADERS,
            'body': json.dumps({
                'message': 'Registration successful',
                'registrationId': registration_id
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