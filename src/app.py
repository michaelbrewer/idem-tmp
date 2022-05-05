import time
from os import environ
from uuid import uuid4

import boto3
from aws_lambda_powertools.utilities.idempotency import DynamoDBPersistenceLayer, IdempotencyConfig, idempotent

DYNAMODB_TABLE = environ["DYNAMODB_TABLE"]
config = IdempotencyConfig(
    function_timeout_clean_up=True,
    event_key_jmespath="uuid",
    use_local_cache=True,
    raise_on_no_idempotency_key=True,
)
boto3_config = boto3.session.Session()
persistence_layer = DynamoDBPersistenceLayer(table_name=DYNAMODB_TABLE, boto3_session=boto3_config)


@idempotent(persistence_store=persistence_layer, config=config)
def handler(event, context):
    time.sleep(4)
    uuid_value: str = str(uuid4())
    return {"message": uuid_value}
