
    schema = {
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["username", "email"],
            "properties": {
                "username": {
                    "bsonType": "string",
                    "description": "Username must be a string."
                },
                "email": {
                    "bsonType": "string",
                    "description": "Email must be a string."
                }
            }
        }
    }

The above is an example to create a schema for validation purposes. This does not create migrations.

Write a code that create such dict and then passes it to the validation method of pymongo.collections.Collection class
