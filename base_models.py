import ipdb
from pymongo.collection import Collection
import inflection

from base_fields import MongoField
from database_connection import DefaultDatabase


class BaseModelCollection(Collection):

    @classmethod
    def extend_json_shema_validation(cls, json_shema):
        class_vars = vars(cls)
        validation_schema = json_shema['$jsonSchema']
        validation_schema['properties'] = {}
        for var in class_vars:
            # ipdb.set_trace()
            if isinstance(class_vars[var], MongoField):
                print(var)
                validation_schema['properties'][str(inflection.camelize(var, False))] = class_vars[var].get_field_validation_data()
        validation_schema['required'] = []
        for var in validation_schema['properties']:
            if validation_schema['properties'][var].get('required') is True:
                validation_schema['properties'][var].pop('required')
                validation_schema['required'].append(var)
        return json_shema
