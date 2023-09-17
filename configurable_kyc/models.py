# Create your flexible models here.
from base_fields import MongoField
from base_models import BaseModelCollection
from database_connection import DEFAULT_DB

assert DEFAULT_DB is not None


class KYC(BaseModelCollection):

    Name = MongoField(
        label='Name',
        extraDescription='Your name that will be used for our correspendence',
        description='Name is required',
        required=True,
        bsonType='string',
    )
    Income = MongoField(
        label='Income (in USD)',
        extraDescription='Your income in USD',
        description='Income needs to be in a number',
        bsonType='long',
    )
    LastIncomeTaxPaid = MongoField(
        label='Last income tax paid (in USD)',
        extraDescription='Please mention the correct amount in USD',
        description='The value should be a number',
        bsonType='int',
        required=True,
    )

    class Meta:
        schema_validation = 'Moderate'
