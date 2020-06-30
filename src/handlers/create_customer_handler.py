from lambda_decorators import (
    load_json_body, json_schema_validator,
    cors_headers, json_http_resp)
from src.entities.customers import Customer
from src.data.create_customer import create_customer

request_schema = {
    'type': 'object',
    'properties': {
        'body': {
            'type': 'object',
            'properties': {
                'customer_id': {'type': 'string'},
                'profile_data': {'type': 'object'}
            },
            'required': ['customer_id', 'profile_data']
        }
    },
    'required': ['body'],
}


@load_json_body  # Doing this first is required for the schema to validate
@json_schema_validator(request_schema=request_schema)
@cors_headers
@json_http_resp
def handler(event, context):
    customer = Customer(**event['body'])
    create_customer(customer)
    if event.get('error'):
        raise Exception(event['error'])
    else:
        return event['body']
