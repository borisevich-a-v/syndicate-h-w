import json
import os
import uuid
import boto3
from datetime import datetime

from commons.log_helper import get_logger
from commons.abstract_lambda import AbstractLambda

_LOG = get_logger('ApiHandler-handler')
dynamodb = boto3.resource('dynamodb')
table_name = os.getenv("target_table_name") or 'Event'
table = dynamodb.Table(table_name)


class ApiHandler(AbstractLambda):

    def validate_request(self, event) -> dict:
        pass

    def handle_request(self, event, context):
        """
        Explain incoming event here
        """

        principal_id = event['principalId']
        content = event['content']
        event_id = str(uuid.uuid4())
        current_time = datetime.now().isoformat()

        event_item = {
            'id': event_id,
            'principalId': principal_id,
            'createdAt': current_time,
            'body': content
        }

        table.put_item(Item=event_item)

        response = {
            'statusCode': 201,
            'event': event_item
        }
        return {
            'statusCode': 201,
            'body': json.dumps(response),
            'headers': {
                'Content-Type': 'application/json'
            }
        }


HANDLER = ApiHandler()


def lambda_handler(event, context):
    return HANDLER.lambda_handler(event=event, context=context)
