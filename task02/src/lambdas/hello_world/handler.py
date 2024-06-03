from commons.log_helper import get_logger
from commons.abstract_lambda import AbstractLambda

_LOG = get_logger('HelloWorld-handler')


class HelloWorld(AbstractLambda):

    def validate_request(self, event) -> dict:
        pass

    def handle_request(self, event, context):
        """
        Explain incoming event here
        """
        path = event['rawPath']
        method = event['requestContext']['http']['method']
        if path == '/hello' and method == 'GET':
            return {
                "statusCode": 200,
                "body": {"message": "Hello from Lambda"}
            }

        return {
            "statusCode": 400,
            "body": {
                "message": f"Bad request syntax or unsupported method. Request path: {path}. HTTP method: {method}"
            }
        }


HANDLER = HelloWorld()


def lambda_handler(event, context):
    return HANDLER.lambda_handler(event=event, context=context)
