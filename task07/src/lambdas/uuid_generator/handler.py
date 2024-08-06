import json
import os
import uuid
import boto3
from commons.log_helper import get_logger
from commons.abstract_lambda import AbstractLambda

_LOG = get_logger('UuidGenerator-handler')

s3 = boto3.client('s3')
bucket_name = os.getenv('target_bucket', 'test')


class UuidGenerator(AbstractLambda):

    def validate_request(self, event) -> dict:
        pass

    def handle_request(self, event, context):
        """
        Explain incoming event here
        """
        file_name = event['time']
        content_dict = {
            'ids': [str(uuid.uuid4()) for _ in range(10)]
        }
        content_json = json.dumps(content_dict, indent=4)

        s3.put_object(Body=content_json, Bucket=bucket_name, Key=file_name, ContentType="application/json")
        return 200


HANDLER = UuidGenerator()


def lambda_handler(event, context):
    return HANDLER.lambda_handler(event=event, context=context)
