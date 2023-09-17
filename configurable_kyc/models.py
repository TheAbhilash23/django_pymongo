# Create your flexible models here.
from base_fields import MongoField
from base_models import BaseModelCollection
from database_connection import DEFAULT_DB

assert DEFAULT_DB is not None


class KYC(BaseModelCollection):

    Name = MongoField(
        label='Name',
        description='Your name that will be used for our correspendence',
        error_description='Name is required',
        required=True,
        bson_type='string',
    )
    Income = MongoField(
        label='Income (in USD)',
        description='Your income in USD',
        error_description='Income needs to be in a number',
        bson_type='long',
    )
    LastIncomeTaxPaid = MongoField(
        label='Last income tax paid (in USD)',
        description='Please mention the correct amount in USD',
        error_description='The value should be a number',
        bson_type='int',
    )

    class Meta:
        schema_validation = 'Moderate'
