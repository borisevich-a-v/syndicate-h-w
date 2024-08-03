import json
import uuid

from commons.log_helper import get_logger
from commons.abstract_lambda import AbstractLambda
import boto3
import os

_LOG = get_logger('AuditProducer-handler')
dynamodb = boto3.resource('dynamodb')
audit_table_name = os.getenv("audit_table_name") or 'cmtr-c4f5c11f-Audit'

audit_table = dynamodb.Table(audit_table_name)


class AuditProducer(AbstractLambda):

    def validate_request(self, event) -> dict:
        pass
        
    def handle_request(self, event, context):
        _LOG.info("Start my code")

        record = event['Records'][0]['dynamodb']
        _LOG.info("Got record: %s", record)

        item_key = record['Keys']['key']['S']
        _LOG.info("item_key: %s", item_key)

        value = record['NewImage']['value']['N']
        _LOG.info("value: %s", value)

        event_item = {
            'id': str(uuid.uuid4()),
            'itemKey': item_key,
            'modificationTime': int(record['ApproximateCreationDateTime']),
            'newValue': {'key': item_key, 'value': value}
        }
        _LOG.info("value: %s", event)

        _LOG.info("audit table: %s", audit_table)

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
