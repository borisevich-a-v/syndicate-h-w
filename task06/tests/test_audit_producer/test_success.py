from unittest.mock import Mock

from tests.test_audit_producer import AuditProducerLambdaTestCase


class TestSuccess(AuditProducerLambdaTestCase):

    def test_success(self):
        event = {
            "Records": [
                {
                    "eventID": "6ab769524543f9b106b8d64fd977f8d3",
                    "eventName": "INSERT",
                    "eventVersion": "1.1",
                    "eventSource": "aws:dynamodb",
                    "awsRegion": "eu-central-1",
                    "dynamodb": {
                        "ApproximateCreationDateTime": 1722675751.0,
                        "Keys": {
                            "key": {
                                "S": "par"
                            }
                        },
                        "NewImage": {
                            "value": {
                                "N": "100"
                            },
                            "key": {
                                "S": "par"
                            }
                        },
                        "SequenceNumber": "2500000000070286110242",
                        "SizeBytes": 19,
                        "StreamViewType": "NEW_AND_OLD_IMAGES"
                    },
                    "eventSourceARN": "arn:aws:dynamodb:eu-central-1:905418349556:table/cmtr-c4f5c11f-Configuration/stream/2024-08-03T08:58:04.429"
                }
            ]
        }

        # self.HANDLER.handle_request(event, Mock())

