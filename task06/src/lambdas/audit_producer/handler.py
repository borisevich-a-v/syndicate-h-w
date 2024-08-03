import json
import uuid
from datetime import datetime

from commons.log_helper import get_logger
from commons.abstract_lambda import AbstractLambda
import boto3
import os

_LOG = get_logger('AuditProducer-handler')
dynamodb = boto3.resource('dynamodb')
conf_table_name = os.getenv("conf_table_name") or 'Configuration'
audit_table_name = os.getenv("audit_table_name") or 'Audit'

conf_table = dynamodb.Table(conf_table_name)
audit_table = dynamodb.Table(audit_table_name)



class AuditProducer(AbstractLambda):

    def validate_request(self, event) -> dict:
        pass
        
    def handle_request(self, event, context):

        record = event['Records'][0]['dynamodb']

        item_key = record['Keys']['key']['S']
        value = record['NewImage']['value']['N']


        event_item = {
            'id': str(uuid.uuid4()),
            'itemKey': item_key,
            'modificationTime': record['ApproximateCreationDateTime'],
            'newValue': {'key': item_key, 'value': value}
        }

        audit_table.put_item(Item=event_item)

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
    

HANDLER = AuditProducer()


def lambda_handler(event, context):
    return HANDLER.lambda_handler(event=event, context=context)
