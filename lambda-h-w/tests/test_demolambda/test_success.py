from tests.test_demolambda import DemolambdaLambdaTestCase


class TestSuccess(DemolambdaLambdaTestCase):

    def test_success(self):
        self.assertEqual(
            self.HANDLER.handle_request(dict(), dict()), {"statusCode": 200,
                                                          "message": "Hello from Lambda"}
        )
