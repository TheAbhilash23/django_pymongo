# Create your flexible models here.
import base_fields
from base_models import BaseModelCollection
from database_connection import DEFAULT_DB

assert DEFAULT_DB is not None


class KYC(BaseModelCollection):

    Name = base_fields.MongoField(
        label='Name',
        extraDescription='Your name that will be used for our correspendence',
        description='Name is required',
        required=True,
        bsonType='string',
    )
    Income = base_fields.MongoField(
        label='Income (in USD)',
        extraDescription='Your income in USD',
        description='Income needs to be in a number',
        bsonType='long',
    )
    LastIncomeTaxPaid = base_fields.MongoField(
        label='Last income tax paid (in USD)',
        extraDescription='Please mention the correct amount in USD',
        description='The value should be a number',
        bsonType='int',
        required=True,
    )
    Address = base_fields.NestedMongoField(
        label='Permanent address or address for correspondence',
        extraDescription='Your address as mentioned on a recognised address proof document.',
        description="The address can't contain (?, /, < and >)",
        #NOTE: Following commented code is also one of the ways you can make nested fields,
        # BUT, it will be hard to debug because it is a dictionary.
        # If it were class attrributes then it would be intuitive and easy to debug.
        # So instead We will go with dunder attributes.
        # *** DO NOT REMOVE THIS COMMENT ***

        # nestedFields={
        #     'addressLine1': base_fields.MongoField(
        #         label='Address Line 1',
        #         description='Only alphanumeric inputs can be stored.',
        #         bsonType='string',
        #         ),
        #     'addressLine2': base_fields.MongoField(
        #         label='Address Line 2',
        #         description='Only alphanumeric inputs can be stored.',
        #         bsonType='string',
        #         ),
        # },
    )
    Address__AddressLine1 = base_fields.MongoField(
                label='Address Line 1',
                description='Only alphanumeric inputs can be stored.',
                bsonType='string',
    )
    Address__AddressLine2 = base_fields.MongoField(
                label='Address Line 2',
                description='Only alphanumeric inputs can be stored.',
                bsonType='string',
    )

    class Meta:
        schema_validation = 'Moderate'
